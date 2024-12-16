from django import forms
from .models import Testimoni

class TestimoniForm(forms.ModelForm):
    class Meta:
        model = Testimoni
        fields = ['keterangan', 'rating']  # Menambahkan rating dan keterangan ke form

    # Widget untuk menampilkan rating bintang 1-5
        rating = forms.ChoiceField(
        choices=[(str(i), f'{i} Bintang') for i in range(1, 6)],
        widget=forms.RadioSelect,
        label="Penilaian (Bintang)"
    )