# Generated by Django 5.1.3 on 2024-12-13 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran', '0018_alter_pendaftaran_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendaftaran',
            name='status',
            field=models.CharField(choices=[('active', 'Aktif'), ('inactive', 'Tidak Aktif')], default='active', max_length=10),
        ),
    ]
