# Generated by Django 2.2.6 on 2019-10-09 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0016_auto_20191009_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='rn',
        ),
    ]
