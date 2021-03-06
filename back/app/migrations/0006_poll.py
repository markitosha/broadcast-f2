# Generated by Django 3.1.5 on 2021-01-24 08:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_broadcast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('question', models.CharField(max_length=255, verbose_name='question')),
                (
                    'first_answer',
                    models.CharField(max_length=255, verbose_name='first_answer'),
                ),
                (
                    'second_answer',
                    models.CharField(max_length=255, verbose_name='second_answer'),
                ),
                (
                    'first_answer_percentage',
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
            ],
        ),
    ]
