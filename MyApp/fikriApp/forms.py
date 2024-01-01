from django import forms
from django.forms import ModelForm
from .models import Berita

from . import models


class FormBerita(ModelForm):

    class Meta:
        model = Berita
        fields = ('nama_berita', 'text_berita')
        labels = {
            'nama_berita': ('Nama Berita'),
            'text_berita': ('Text Berita'),
            
           
            }
