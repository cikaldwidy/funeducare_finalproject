# Generated by Django 5.1.3 on 2024-12-09 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_customuser_no_telp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='no_telp',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
