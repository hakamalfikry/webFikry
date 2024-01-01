from django.urls import path
from . import views

urlpatterns =[
    path('index/', views.index, name='index'),
    path('berita/', views.berita, name='berita'),
    path('addberita/', views.addBerita, name='addberita'),
    path('contact/', views.contact, name='cotact'),
    path('about/', views.about, name='about'),
]