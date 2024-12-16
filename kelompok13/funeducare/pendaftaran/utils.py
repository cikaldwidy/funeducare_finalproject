from midtransclient import Snap
from django.conf import settings
import uuid
import requests
from .models import Pendaftaran

def create_payment_link(pendaftaran):
    snap = Snap(
        is_production=settings.MIDTRANS_IS_PRODUCTION,
        server_key=settings.MIDTRANS_SERVER_KEY,
        client_key=settings.MIDTRANS_CLIENT_KEY
    )

    # Buat order_id unik dengan UUID
    order_id = f'ORDER-{str(uuid.uuid4())}'

    transaction_details = {
        'order_id': order_id,
        'gross_amount': float(pendaftaran.get_price())
    }

    item_details = [{
        'id': f'PROGRAM-{pendaftaran.program.id}',
        'price': float(pendaftaran.get_price()),
        'quantity': 1,
        'name': pendaftaran.program.name
    }]

    customer_details = {
        'first_name': pendaftaran.nama_ortu.first_name,  # Parent's first name
        'email': pendaftaran.nama_ortu.email,  # Parent's email
        'child_name': pendaftaran.nama_anak.nama_anak,  # Child's name
        'program': pendaftaran.program.name,  # Program name    
        }

    transaction = {
        'transaction_details': transaction_details,
        'item_details': item_details,
        'customer_details': customer_details,
        'expiry': {
            'unit': 'minutes',
            'duration': 30  # Waktu kadaluarsa pembayaran 30 menit
        }
    }

    snap_response = snap.create_transaction(transaction)

    # Update Pendaftaran dengan payment_url dan order_id
    pendaftaran.payment_url = snap_response['redirect_url']
    pendaftaran.order_id = order_id
    pendaftaran.payment_status = 'pending'
    pendaftaran.save()

    return snap_response

def check_payment_status(order_id):
    try:
        pendaftaran = Pendaftaran.objects.get(order_id=order_id)
        
        # URL endpoint untuk cek status pembayaran
        url = f"https://api.midtrans.com/v2/{order_id}/status"
        
        # Header dengan authorization menggunakan server key
        headers = {
            'Authorization': f'Basic {settings.MIDTRANS_SERVER_KEY}',
            'Content-Type': 'application/json'
        }
        
        # Kirim request GET ke Midtrans API untuk mendapatkan status pembayaran
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            transaction_status = data.get('transaction_status')
            
            # Update status pembayaran sesuai dengan status baru
            if transaction_status == 'settlement':
                pendaftaran.payment_status = 'success'  # Change to success
            elif transaction_status == 'pending':
                pendaftaran.payment_status = 'pending'
            elif transaction_status in ['deny', 'cancel']:
                pendaftaran.payment_status = 'failed'
            
            # Removed 'expire' since 'expired' status is no longer used
            pendaftaran.save()
            return transaction_status
        
        return None
    except Pendaftaran.DoesNotExist:
        return None
    
def handle_payment_notification(notification):
    try:
        order_id = notification['order_id']
        transaction_status = notification['transaction_status']
        
        pendaftaran = Pendaftaran.objects.get(order_id=order_id)
        
        # Update payment status based on transaction status
        if transaction_status == 'settlement':
            pendaftaran.payment_status = 'success'  # Change to success
        elif transaction_status == 'pending':
            pendaftaran.payment_status = 'pending'
        elif transaction_status in ['deny', 'cancel']:
            pendaftaran.payment_status = 'failed'
        
        pendaftaran.save()
        return True
    except Pendaftaran.DoesNotExist:
        return False
