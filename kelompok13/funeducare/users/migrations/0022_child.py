# Generated by Django 5.1.3 on 2024-12-09 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_customuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_anak', models.CharField(max_length=100)),
                ('jenis_kelamin', models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=10)),
                ('hobi', models.CharField(max_length=255)),
                ('riwayat_penyakit', models.TextField()),
                ('program', models.CharField(max_length=255)),
                ('usia', models.IntegerField()),
                ('keterangan_tambahan', models.TextField(blank=True, null=True)),
                ('foto_anak', models.ImageField(blank=True, null=True, upload_to='child_profiles/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
