from django.db import models

# Create your models here.
class Berita(models.Model):
    nama_berita = models.CharField(max_length=10)
    text_berita = models.TextField()
    gambar_berita = models.ImageField()


    def __unicode__(self):
        return self.nama_berita



