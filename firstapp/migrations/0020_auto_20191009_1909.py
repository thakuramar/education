# Generated by Django 2.2.6 on 2019-10-10 00:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0019_auto_20191009_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rn',
            field=models.IntegerField(blank=True, default='DEFAULT VALUE', validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
