# Generated by Django 3.1 on 2020-09-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200912_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='age_limit',
            field=models.IntegerField(blank=True, choices=[(0, 'kids'), (1, 'teens'), (2, 'adults')], null=True),
        ),
    ]
