# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0006_auto_20190323_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='bus_image',
        ),
        migrations.AddField(
            model_name='business',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logo/'),
        ),
    ]
