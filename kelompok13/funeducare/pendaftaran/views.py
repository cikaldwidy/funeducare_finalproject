# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import BookingForm
from .models import Pendaftaran
from .utils import create_payment_link
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.conf import settings
from django.http import JsonResponse
from programs.models import Fee
from .utils import handle_payment_notification, check_payment_status
  # Pastikan nama modul sudah benar


def pendaftaran(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES, user=request.user)
        
        if form.is_valid():
            selected_child = form.cleaned_data['nama_anak']
            program = form.cleaned_data['program']
            fee = form.cleaned_data['fee']
            
            pendaftaran = Pendaftaran.objects.create(
                nama_ortu=request.user,
                nama_anak=selected_child,
                program=program,
                fee=fee,
            )
            
            snap_response = create_payment_link(pendaftaran)
            if 'redirect_url' in snap_response:
                pendaftaran.payment_url = snap_response['redirect_url']
                pendaftaran.save()
                
                return render(request, 'payment.html', {
                    'payment_url': snap_response['redirect_url'],
                    'program_name': pendaftaran.program.name,
                    'fee_type': pendaftaran.fee.type_program,
                    'amount': pendaftaran.get_price()
                })
            else:
                return render(request, 'payment_error.html', {'error': 'Gagal membuat link pembayaran'})
    else:
        # Passing user ke form untuk filtering
        form = BookingForm(user=request.user)
    
    return render(request, 'form_booking.html', {'form_booking': form})

def syarat(request):
    return render(request, 'syarat.html')


def cara_mendaftar(request):
    return render(request, 'cara_mendaftar.html')


def get_fees(request):
    program_id = request.GET.get('program_id')
    fees = Fee.objects.filter(program_id=program_id).values('id', 'type_program', 'amount')
    return JsonResponse({'fees': list(fees)})


@csrf_exempt
def payment_notification(request):
    if request.method == 'POST':
        try:
            notification = json.loads(request.body)
            
            if handle_payment_notification(notification):
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=404)
        except Exception as e:
            # Log error
            return HttpResponse(status=400)
    
    return HttpResponse(status=400)


def update_payment_status(request, order_id):
    payment_status = check_payment_status(order_id)
    
    if payment_status:
        return JsonResponse({
            'status': 'success', 
            'payment_status': payment_status
        })
    else:
        return JsonResponse({
            'status': 'error', 
            'message': 'Order not found or error in fetching payment status'
        })
