from django.db import models
from django.utils import timezone
from programs.models import Program, Fee
from users.models import Child
from django.conf import settings
import uuid
class Pendaftaran(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'), 
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('failed', 'Failed'),
        ('success', 'Success'),
    ]
    
    # Menghubungkan nama_ortu ke model User (CustomUser)
    nama_ortu = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name="Nama Orang Tua",
        null=True, blank=True
    )
    
    # Menghubungkan nama_anak ke model Child
    nama_anak = models.ForeignKey(
        Child, 
        on_delete=models.CASCADE, 
        verbose_name="Nama Anak",
        blank=True, null=True
    )

    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name="Program")
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE, verbose_name="Jenis Program")

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending'  # Default status adalah 'pending'
    )
    
    payment_url = models.CharField(max_length=255, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    # Status Pendaftaran (Aktif atau Tidak Aktif)
    STATUS_CHOICES = [
        ('active', 'Aktif'),
        ('inactive', 'Tidak Aktif'),
    ]
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'  # Default status adalah 'active'
    )

    def generate_custom_id(self):
        return f"PRG-{str(self.id)[:5]}" 
    
    def __str__(self):
        return f"{self.nama_ortu} - {self.nama_anak}"
    
    def get_price(self):
        return self.fee.amount if self.fee else 0

    def update_payment_status(self, status, transaction_id=None, payment_url=None):
        """Method to update the payment status after transaction response"""
        self.payment_status = status
        if transaction_id:
            self.transaction_id = transaction_id
        if payment_url:
            self.payment_url = payment_url
        self.save()

    # Optional: You can also define other helper methods, such as determining whether the payment is successful
    def is_payment_successful(self):
        return self.payment_status == 'success'

    def is_payment_failed(self):
        return self.payment_status == 'failed'

    def is_payment_pending(self):
        return self.payment_status == 'pending'

    def check_status(self):
        """Memeriksa apakah pendaftaran terkait program sudah berakhir dan mengupdate statusnya."""
        if self.program.program_end_date and self.program.program_end_date < timezone.now():
            self.status = 'inactive'
        self.save()