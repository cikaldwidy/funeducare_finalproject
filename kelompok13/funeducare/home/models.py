from django.conf import settings
from django.db import models


class Testimoni(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # Menghubungkan dengan user yang login
    keterangan = models.TextField()  # Isi testimoni
    rating = models.IntegerField(choices=[(i, f'{i} Bintang') for i in range(1, 6)])  # Rating bintang 1-5
    is_approved = models.BooleanField(default=False)  # Status validasi oleh admin
    
    def __str__(self):
        return f"Testimoni dari {self.user.username if self.user else 'Anonymous'}"
class Fasilitas(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    foto = models.FileField(upload_to='fasilitas/')

    def __str__(self):
        return f"{self.id} - {self.judul}"