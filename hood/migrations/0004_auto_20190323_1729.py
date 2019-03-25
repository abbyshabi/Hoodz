# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_remove_project_join'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='logo',
        ),
        migrations.AddField(
            model_name='business',
            name='image',
            field=models.ImageField(blank=True, upload_to='logo/'),
        ),
    ]
