# Generated by Django 3.1.5 on 2021-01-29 06:43

import app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210124_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=app.models.OwnPhoneNumberField(error_messages={'unique': 'Пользователь с таким номером телефона уже существует.'}, max_length=128, region=None, unique=True, verbose_name='phone'),
        ),
    ]
