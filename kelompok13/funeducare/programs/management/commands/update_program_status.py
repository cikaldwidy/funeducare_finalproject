from django.core.management.base import BaseCommand
from datetime import datetime
from programs.models import Program

class Command(BaseCommand):
    help = 'Update status program berdasarkan tanggal selesai'

    def handle(self, *args, **kwargs):
        programs = Program.objects.all()  # Ambil semua program
        for program in programs:
            program.check_status()  # Periksa dan perbarui status program
        self.stdout.write(self.style.SUCCESS('Successfully updated program statuses'))
