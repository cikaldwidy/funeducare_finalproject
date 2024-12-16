from django.shortcuts import render
from .models import Guru, Galeri

def aboutus_view(request):
    gurus = Guru.objects.all()
    galeris = Galeri.objects.all().order_by('-created_at')
    return render(request, 'aboutus/aboutus.html', {
        'gurus': gurus,
        'galeris': galeris
    })
