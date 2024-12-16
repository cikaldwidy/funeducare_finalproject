from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import  login,logout
from .forms import SignupForm,LoginForm,ChangePasswordUserForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import Child,ChildDevelopment
from .forms import ChildProfileForm
from pendaftaran.models import Pendaftaran
from django.utils import timezone
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import inch


@login_required
def user_logout(request):
    logout(request)
    next_url = request.GET.get('next', '/') 
    return redirect(next_url)  


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save() 
            email = form.cleaned_data['email'] 
            name = form.cleaned_data['username']
            login_url = request.build_absolute_uri('/users/login/')
            send_mail(
            'Selamat, Registrasi Sukses!',
            f'Halo {name},\n\nTerima kasih telah bergabung dengan FunEduCare! Akun Anda berhasil dibuat dan Anda sudah siap memulai petualangan belajar bersama kami.\n\nUntuk mengakses layanan kami dan melanjutkan, silakan login ke akun Anda dengan mengklik tautan berikut:\n{login_url}\n\nJika Anda mengalami kendala saat mengakses akun atau memiliki pertanyaan lebih lanjut, silakan hubungi kami di funeducare.id@gmail.com.\n\nSelamat bergabung dan selamat belajar!',
            'funeducare.id@gmail.com', #email funeducare
            [email],  # Email tujuan 
            fail_silently=False,
)
            messages.success(request, 'Pendaftaran berhasil ! Silakan login.')
        else:
            messages.error(request, 'Ada kesalahan saat pengisian form. Mohon isi ulang kembali !')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  
        if form.is_valid():  # form valid ( validasi captcha)
            user = form.get_user() 
            login(request, user)  # Login user ke session
            messages.success(request, f'Selamat datang {request.user.username} ! Sekarang kamu bagian dari keluarga Funeducare.id') 
            return redirect('home:home')  # Redirect ke halaman home setelah login berhasil
        else:
            print(form.errors)  
            if form.errors.get('captcha'):  # Jika ada error di captcha
                messages.error(request, 'reCAPTCHA tidak valid. Pastikan Anda sudah mengisi reCAPTCHA dengan benar.')
            else:
                messages.error(request, 'Email atau password anda salah. Mohon isi ulang kembali')
            return redirect('users:login')  #  form tidak valid, redirect ke halaman login
    else:
        form = LoginForm() 
    
    return render(request, 'login.html', {'form': form})



def change_password(request):
    form = ChangePasswordUserForm(request.user, request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            logout(request)
            messages.success(request, 'Password berhasil diganti ! silahkan login kembali')
            return redirect('users:login')  
        else:
            messages.error(request, 'Password tidak valid, silahkan coba lagi !')
            return redirect('users:change_password')
    
    else:
        form = ChangePasswordUserForm(request.user)
    
    context = {
        'judul': 'Change password',
        'form': form,
    }
    return render(request, 'change_password.html', context)


@login_required
def update_account(request):
    active_pendaftarans = Pendaftaran.objects.filter(
        nama_ortu=request.user,  
        payment_status='success'
    )

    active_programs = []
    for pendaftaran in active_pendaftarans:
        if pendaftaran.status == 'active':
            active_programs.append({
                'program_start_date':pendaftaran.program.program_start_date,
                'program_end_date': pendaftaran.program.program_end_date,
                'id':pendaftaran.generate_custom_id,
                'child_name': pendaftaran.nama_anak.nama_anak, 
                'program_name': pendaftaran.program.name, 
                'program_description': pendaftaran.program.description,  
                'age_range': pendaftaran.program.age_range, 
                'registration_date': pendaftaran.created_at,
                'fee_type': pendaftaran.fee.type_program,  
                'status': pendaftaran.status,
            })

    active_programs.sort(key=lambda x: x['registration_date'], reverse=True)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, user=request.user)
        
        if form.is_valid():
            # Get cleaned data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            alamat = form.cleaned_data.get('alamat', request.user.alamat)
            no_telp = form.cleaned_data.get('no_telp', request.user.no_telp)
            gender = form.cleaned_data.get('gender', request.user.gender)

            changes_made = False

            if request.user.username != username:
                request.user.username = username
                changes_made = True
            if request.user.first_name != first_name:
                request.user.first_name = first_name
                changes_made = True
            if request.user.last_name != last_name:
                request.user.last_name = last_name
                changes_made = True
            if request.user.alamat != alamat:
                request.user.alamat = alamat
                changes_made = True

            # Validasi nomor telepon
            if request.user.no_telp != no_telp:
                if no_telp:  
                    try:
                        validator = RegexValidator(
                            regex=r'^\+?1?\d{9,12}$',
                            message="Nomor telepon harus terdiri dari 9-12 digit dan hanya angka."
                        )
                        validator(no_telp)
                        request.user.no_telp = no_telp
                        changes_made = True
                    except ValidationError as e:
                        messages.error(request, f"Kesalahan pada nomor telepon: {e.message}")
                        return render(request, 'profile.html', {'form': form, 'active_programs': active_programs})  

            if request.user.gender != gender:
                request.user.gender = gender
                changes_made = True

            if form.cleaned_data.get('profile_image'):
                if request.user.profile_image != form.cleaned_data['profile_image']:
                    request.user.profile_image = form.cleaned_data['profile_image']
                    changes_made = True

            if 'delete_image' in request.POST and request.POST['delete_image'] == 'on':
                if request.user.profile_image:
                    request.user.profile_image = None
                    changes_made = True

            if changes_made:
                request.user.save()
                messages.success(request, "Akun berhasil diperbarui")
            else:
                messages.info(request, "Tidak ada perubahan yang dilakukan.")

            return redirect('users:profile-base')
        else:
            if form.errors.get('username'):
                messages.error(request, "Username sudah digunakan! Silakan coba lagi.")
    else:
        form = UserUpdateForm(initial={
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'alamat': request.user.alamat,
            'no_telp': request.user.no_telp,
            'gender': request.user.gender,
        }, user=request.user)

    context = {
        'form': form,
        'active_programs': active_programs,
    }

    return render(request, 'profile.html', context)

def riwayat_pembayaran(request):
    # Ambil user yang sedang login 
    riwayat_pembayaran = Pendaftaran.objects.filter(nama_ortu=request.user).order_by('-created_at')
    
    return render(request, 'riwayat_pembayaran.html', {
        'riwayat_pembayaran': riwayat_pembayaran
    })


def profile(request):
    if request.method == 'POST':
        form = ChildProfileForm(request.POST, request.FILES)  # Mengirimkan request.FILES
        if form.is_valid():  
            child_profile = form.save(commit=False)
            child_profile.user = request.user  
            print(request.FILES)  
            child_profile.save() 
            return redirect('users:profile_view') 
        else:         
            print(form.errors)  
            
    else:
        form = ChildProfileForm()

    return render(request, 'profil_anak.html', {'form': form})


def profile_view(request):
    active_pendaftarans = Pendaftaran.objects.filter(
        nama_ortu=request.user,
        payment_status='success' 
    ) 
    children = Child.objects.filter(user=request.user, is_approved=True)
    pending_children = Child.objects.filter(user=request.user, is_approved=False)
    active_programs = []
    for pendaftaran in active_pendaftarans:
        active_programs.append({
            'program_name': pendaftaran.program.name, 
        })

    context = {
        'children': children,  
        'active_programs': active_programs,  
        'pending_children': pending_children,
    }

    return render(request, 'profile_view.html', context)

def delete_child(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    if request.method == 'POST':
        child.delete()  
        return redirect('users:profile_view')
    return redirect('users:profile_view')
            
def riwayat_kegiatan(request):
    riwayat_pendaftarans = Pendaftaran.objects.filter(
        nama_ortu=request.user,
        payment_status='success'
    )

    riwayat_programs = []
    current_time = timezone.now()
    for pendaftaran in riwayat_pendaftarans:
        if pendaftaran.status == 'inactive' :
            riwayat_programs.append({
                'program_start_date': pendaftaran.program.program_start_date,
                'program_end_date': pendaftaran.program.program_end_date,
                'id': pendaftaran.generate_custom_id(),
                'child_name': pendaftaran.nama_anak.nama_anak,
                'program_name': pendaftaran.program.name,
                'program_description': pendaftaran.program.description,
                'age_range': pendaftaran.program.age_range,
                'registration_date': pendaftaran.created_at,
                'fee_type': pendaftaran.fee.type_program,
                'status': pendaftaran.status,
            })
    riwayat_programs.sort(key=lambda x: x['registration_date'], reverse=True)

    return render(request, 'riwayat_kegiatan.html', {'riwayat_programs': riwayat_programs})

def laporan_perkembangan(request):
    active_pendaftarans = Pendaftaran.objects.filter(
    nama_ortu=request.user,
    payment_status='success' 
    )
    
    children = Child.objects.filter(user=request.user, is_approved=True)
    pending_children = Child.objects.filter(user=request.user, is_approved=False)
    active_programs = []
    for pendaftaran in active_pendaftarans:
        active_programs.append({
            'program_name': pendaftaran.program.name, 
        })

    context = {
        'children': children,  
        'active_programs': active_programs,  
        'pending_children': pending_children,
    }

    return render(request, 'laporan_perkembangan.html', context)


def download_pdf_view(request, child_id):
    try:
        child = Child.objects.get(id=child_id)
        developments = ChildDevelopment.objects.filter(child=child)
    except Child.DoesNotExist:
        return HttpResponse("Child not found.", status=404)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={child.nama_anak}_laporan_perkembangan_anak.pdf'

    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle('PDF Report')

    # Header of the PDF
    pdf.setFont("Helvetica", 10)
    pdf.drawString(100, 750, f"Laporan Perkembangan Anak")

    # Child info
    pdf.drawString(100, 730, f"Nama Anak: {child.nama_anak}")
    pdf.drawString(100, 710, f"Usia: {child.usia} Tahun")
    pdf.drawString(100, 690, f"Jenis Kelamin: {child.jenis_kelamin}")

    y_position = 650

    # Prepare data for the table
    data = [['Kategori', 'Deskripsi', 'Status Perkembangan']]  # Header row
    for development in developments:
        data.append([
            development.get_category_display(),
            development.description,  # Deskripsi panjang
            development.get_level_display()
        ])

    # Define column widths for the table
    col_widths = [2 * inch, 3 * inch, 1.5 * inch]  # Width for each column
    table = Table(data, colWidths=col_widths, style=TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('WORDWRAP', (1, 1), (-1, -1), True)  # Enable text wrapping for the 'Deskripsi' column
    ]))

    # Wrap the content inside each cell (especially for 'Deskripsi')
    # Adjust the row height dynamically based on the content
    table_height = 0
    for i, row in enumerate(data):
        row_height = max(len(row[1]) // 60, 1) * 20  # Rough calculation to fit the description
        table_height += row_height

    # Ensure we don't get any content off-page by wrapping the table and drawing it
    table.wrapOn(pdf, letter[0] - 100, y_position - 20)
    table.drawOn(pdf, 50, y_position - table_height)

    pdf.save()
    return response