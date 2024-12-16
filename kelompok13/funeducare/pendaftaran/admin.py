from django.contrib import admin
from .models import Pendaftaran

@admin.register(Pendaftaran)
class PendaftaranAdmin(admin.ModelAdmin):
    list_display = ('id', 'generate_custom_id', 'created_at', 'nama_ortu', 'nama_anak', 'program')
    list_filter = ('status', 'payment_status', 'program')

    # Menambahkan metode untuk menghasilkan ID kustom
    def generate_custom_id(self, obj):
        return obj.generate_custom_id()
    generate_custom_id.short_description = 'ID Kegiatan'  # Memberi nama kolom ID Kegiatan

