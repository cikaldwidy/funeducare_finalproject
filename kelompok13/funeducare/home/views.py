from django.shortcuts import render, redirect
from .models import Testimoni, Fasilitas
from .forms import TestimoniForm
# Create your views here.

def home_view(request):
    testimonials = Testimoni.objects.filter(is_approved=True)  # Hanya menampilkan testimoni yang disetujui
    rating_range = range(1, 6)
    
    if request.method == 'POST':
        form = TestimoniForm(request.POST)
        if form.is_valid():
            testimoni = form.save(commit=False)
            testimoni.user = request.user  # Menetapkan user yang sedang login sebagai pengirim testimoni
            testimoni.is_approved = False  # Menetapkan status sebagai belum disetujui
            testimoni.save()
            return redirect('home:home')  # Redirect ke halaman yang sama setelah menyimpan testimoni
    else:
        form = TestimoniForm()

    context = {
        'whatsapp_number': '6285536387624',
        'testimonials': testimonials,  # Hanya menampilkan testimoni yang disetujui
        'form': form,
        'rating_range': rating_range,
    }
    
    return render(request, 'home/index.html', context)


def detail_fasilitas(request, fasilitas_id):
    dt = Fasilitas.objects.get(pk=fasilitas_id)
    all_fasilitas = Fasilitas.objects.all()
    return render(request, 'detail_fasilitas.html', {'detail': dt, 'all':all_fasilitas})

def fasilitas(request):
    all_fasilitas = Fasilitas.objects.all()
    return render(request, 'fasilitas.html', {'all':all_fasilitas})



