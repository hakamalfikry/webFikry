# Generated by Django 5.0 on 2024-01-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fikriApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='berita',
            name='gambar_berita',
        ),
        migrations.AlterField(
            model_name='berita',
            name='nama_berita',
            field=models.CharField(max_length=10),
        ),
    ]