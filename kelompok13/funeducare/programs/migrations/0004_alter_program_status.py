# Generated by Django 5.1.3 on 2024-12-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_program_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='status',
            field=models.CharField(choices=[('sedang berlangsung', 'Aktif'), ('sudah selesai', 'Tidak Aktif')], default='active', max_length=20),
        ),
    ]
