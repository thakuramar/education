# Generated by Django 2.2.6 on 2019-10-09 23:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_auto_20191009_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pn',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=15, validators=[django.core.validators.RegexValidator('^0?[5-9]{1\\d{9}$')]),
        ),
    ]
