# Generated by Django 5.1.3 on 2024-12-10 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
        ('users', '0023_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='programs.program'),
        ),
    ]
