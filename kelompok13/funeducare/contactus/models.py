from django.db import models

# Create your models here.
class PostModel(models.Model):
    Nama = models.CharField(max_length=200)
    Email = models.EmailField()
    Nomor_Kontak = models.IntegerField()
    Pesan = models.TextField()
    
    Publish = models.DateTimeField(auto_now_add = True)
        
    def __str__(self):
        return "{}. {}". format(self.id, self.Nama) 