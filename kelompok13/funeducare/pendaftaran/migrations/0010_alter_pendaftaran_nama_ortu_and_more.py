# Generated by Django 5.1.3 on 2024-12-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran', '0009_alter_pendaftaran_nama_ortu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendaftaran',
            name='nama_ortu',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nama Orang Tua'),
        ),
        migrations.AlterField(
            model_name='pendaftaran',
            name='umur_anak',
            field=models.CharField(max_length=2, verbose_name='Umur Anak'),
        ),
    ]
