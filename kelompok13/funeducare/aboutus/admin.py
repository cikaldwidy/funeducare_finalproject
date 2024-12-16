from django.contrib import admin
from .models import Guru, Galeri

@admin.register(Guru) 
class GuruAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at','nama', 'deskripsi_singkat')
    search_fields = ('nama', 'deskripsi_singkat')
    readonly_fields = ('id', 'created_at')
    
@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'judul')
    search_fields = ('judul',)
    readonly_fields = ('id', 'created_at')
