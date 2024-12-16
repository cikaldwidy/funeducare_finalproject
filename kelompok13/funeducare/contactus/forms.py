from django import forms

class ContactForm(forms.Form):
    Nama = forms.CharField(
        label = 'Nama',
        max_length=200,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Masukkan nama Anda'
            }
            
        )
    )
    Email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Masukkan email Anda'
            }
            
        )
    )
    Nomor_Kontak = forms.IntegerField(
        label = 'Nomor Kontak',
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Masukkan nomor kontak Anda'
            }
            
        )
    )
    Pesan = forms.CharField(
        label = 'Pesan',
        widget = forms.Textarea(
            attrs = {
                'class':'form-control',
                'placeholder':'Masukkan pesan Anda'
            }
        )
    )
    
    # name = forms.CharField(label='Name', max_length=100, required=True)
    # email = forms.EmailField(label='Email', required=True)
    # contact = forms.CharField(label='Contact Number', max_length=20, required=True)
    # message = forms.CharField(label='Message', widget=forms.Textarea, required=True)