from django import forms

class ProgramsCompetitionForm(forms.Form):
  nama = forms.CharField(
    label='Nama Lengkap Anak',
    max_length=25,
    widget=forms.TextInput(
      attrs={
        'class':'form-control',
        'placeholder' : 'Masukkan nama lengkap anak anda'
      }
    )
  )
  email = forms.EmailField(
    help_text="Masukkan email anda dengan benar. Contoh: user@gmail.com"
  )
  jenkel = forms.ChoiceField(
    label='Jenis Kelamin',
    widget=forms.RadioSelect(
      attrs={
      'class':'form-check-input',
      }
    ),
    choices=[
      ('l', 'Laki-Laki'),
      ('p', 'Perempuan'),
    ]
  )
  tgl_lahir = forms.DateField(
    label='Tanggal Lahir',
    widget=forms.SelectDateWidget(years=range(2016, 2022, 1), attrs={
      'class':'form-select',
    }))
  pesan = forms.CharField(
    widget=forms.Textarea(
      attrs={
        'class':'form-control',
        'placeholder':'Masukkan pesan anda'
      }
    ))
  agree = forms.BooleanField(
    label="Saya setuju untuk mengikuti lomba dan mengikuti syarat dan ketentuan yang berlaku", 
  )

  email.widget.attrs.update({'class':'form-control', 'placeholder':'Masukkan email anda'})

