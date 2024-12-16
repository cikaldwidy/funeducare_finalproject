from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import CustomUser,Child,ChildDevelopment
from django_recaptcha.fields import ReCaptchaField
import re
class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label="Nama Depan",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Nama Depan '})
    )
    last_name = forms.CharField(
        required=True,
        label="Nama Belakang",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Nama Belakang '})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Email Anda'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Password '})
    )
    password2 = forms.CharField(
        label="Verifikasi Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Ulang Password '})
    )

    class Meta:
        model = get_user_model()  # Use the custom user model here
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Username Anda'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email sudah digunakan oleh pengguna lain.")
        return email

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=30,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    captcha = ReCaptchaField()
    
class ChangePasswordUserForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
        
        
class UserUpdateForm(forms.Form):
    username = forms.CharField(
    max_length=20,
    label='Username',
    widget=forms.TextInput(attrs={'placeholder': 'Masukkan username Anda'})
    )
    first_name = forms.CharField(
    max_length=10, 
    label='First Name',
    widget=forms.TextInput(attrs={'placeholder': 'Masukkan nama depan'})
    )
    last_name = forms.CharField(
    max_length=10,
    label='Last Name',
    widget=forms.TextInput(attrs={'placeholder': 'Masukkan nama belakang'})
    )  
    profile_image = forms.ImageField(required=False, label='Profile Image')
    alamat = forms.CharField(
    max_length=255, 
    required=False,
    label='Alamat',
    widget=forms.TextInput(attrs={'placeholder': 'Masukkan alamat Anda'})  
    )  # Address field
    gender_choices = [('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')]  # Gender options
    gender = forms.ChoiceField(choices=gender_choices, required=False, label='Jenis Kelamin')
    no_telp = forms.CharField(
    max_length=12,
    required=False,
    label='No Telp',
    widget=forms.TextInput(attrs={'placeholder': 'Masukkan Nomor Telepon'})
    )

    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        # Check if username already exists, excluding the current user
        if CustomUser.objects.filter(username__iexact=username).exclude(id=self.user.id).exists():
            raise forms.ValidationError("Username sudah terdaftar! Pilih username lain.")
        return username
    def clean_no_telp(self):
        no_telp = self.cleaned_data.get('no_telp')
        if no_telp and not re.match(r'^\+?1?\d{12}$', no_telp):
            raise forms.ValidationError("Nomor telepon tidak valid.")
        return no_telp
    


# child profile
# forms.py

class ChildProfileForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['nama_anak', 'usia', 'jenis_kelamin', 'hobi', 'program', 'riwayat_penyakit', 'keterangan_tambahan', 'foto_anak', 'akta_kelahiran', 'ktp']
        widgets = {
            'keterangan_tambahan': forms.Textarea(attrs={'class':'form-area'}),  # Menambahkan cols dan rows
            'riwayat_penyakit': forms.Textarea(attrs={'class':'form-area'}),  # Menambahkan cols dan rows
            'foto_anak': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'akta_kelahiran': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ktp': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()

        # Menambahkan validasi kustom, misalnya memastikan 'nama_anak' tidak kosong
        if not cleaned_data.get('nama_anak'):
            self.add_error('nama_anak', 'Nama anak harus diisi.')
        if not cleaned_data.get('jenis_kelamin'):
            self.add_error('jenis_kelamin', 'Jenis kelamin harus diisi.')
        if not cleaned_data.get('riwayat_penyakit'):
            self.add_error('hobi', 'Riwayat penyakit harus diisi.')
        if not cleaned_data.get('ktp'):
            self.add_error('ktp', 'Foto anak harus diisi.')
        if not cleaned_data.get('akta_kelahiran'):
            self.add_error('akta_kelahiran', 'Nama anak harus diisi.')

        # Tambahkan validasi untuk field lainnya sesuai kebutuhan

        return cleaned_data
    
