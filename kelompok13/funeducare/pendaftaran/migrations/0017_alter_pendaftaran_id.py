# Generated by Django 5.1.3 on 2024-12-13 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran', '0016_alter_pendaftaran_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendaftaran',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
