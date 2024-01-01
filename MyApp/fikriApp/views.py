from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Berita
from . import forms
from .forms import FormBerita
from django.contrib import messages

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render() )

def berita(request):
    berita = Berita.objects.all()
    context = {
        "berita" : berita
    }
    
    return render(request, 'berita.html', context)



def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render() )

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render() )

def addBerita(request):
    if request.method == 'POST':
        form = FormBerita(request.POST)
        if form.is_valid():
            new_berita = FormBerita(request.POST)
            new_berita.save()
            messages.success(request, 'Sukses Menambah Berita')
            return redirect('berita')
    else:
        form = FormBerita()
    return render(request, 'addberita.html',{'form':form})

