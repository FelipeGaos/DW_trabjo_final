# Generated by Django 2.0.6 on 2018-06-24 00:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='usuario',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
