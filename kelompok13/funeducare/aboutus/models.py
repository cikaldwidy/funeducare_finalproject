from django.db import models
from django.utils import timezone

class Guru(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    nama = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='guru_photos/', null=True, blank=True)
    deskripsi_singkat = models.TextField()
    deskripsi_detail = models.TextField()

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Guru"
        
class Galeri(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    judul = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='galeri_photos/', null=True, blank=True)
    deskripsi_detail = models.TextField()

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name_plural = "Galeri"

