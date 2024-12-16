from django.shortcuts import render 
from .forms import ContactForm
from .models import PostModel 
from django.contrib import messages

# Create your views here.
# def contactus_view(request):
#     return render(request,'contactus/contactus.html')

def contactus_view(request):
    post_form = ContactForm()
    
    # if request.method == 'POST':
        
        
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            PostModel.objects.create(
                Nama = request.POST.get('Nama'),
                Email = request.POST.get('Email'),
                Nomor_Kontak = request.POST.get('Nomor_Kontak'),
                Pesan = request.POST.get('Pesan'),
            )
            messages.success(request, 'Pesan berhasil dikirim!')
        else:
            messages.error(request, 'Ada kesalahan saat pengisian form.')
            
    context = {
        'post_form' : post_form
    }
    
    return render(request,'contactus/contactus.html', context)