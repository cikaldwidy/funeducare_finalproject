# Generated by Django 5.1.3 on 2024-12-13 01:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran', '0015_alter_pendaftaran_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendaftaran',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
