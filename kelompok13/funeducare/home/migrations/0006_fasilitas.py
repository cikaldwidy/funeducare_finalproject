# Generated by Django 5.1.3 on 2024-12-07 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_testimoni_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fasilitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
                ('foto', models.FileField(upload_to='fasilitas/')),
            ],
        ),
    ]
