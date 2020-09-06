# Generated by Django 3.1.1 on 2020-09-06 07:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_genre_age_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='age_limit',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(18), django.core.validators.MinValueValidator(1)]),
        ),
    ]
