# Generated by Django 5.1.3 on 2024-12-13 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_program_program_end_date_program_program_start_date'),
        ('users', '0026_child_is_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiwayatKegiatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_selesai', models.DateTimeField()),
                ('catatan', models.TextField(blank=True, null=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.program')),
            ],
        ),
    ]
