# Generated by Django 2.2.6 on 2019-10-10 00:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0025_auto_20191009_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rn',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]