from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['nomi', 'rejissyor', 'chiqarilgan_yil', 'janr', 'reyting']