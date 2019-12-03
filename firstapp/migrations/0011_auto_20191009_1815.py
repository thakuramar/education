# Generated by Django 2.2.6 on 2019-10-09 23:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_auto_20191009_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pn',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='rn',
            field=models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]