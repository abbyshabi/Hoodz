# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='bus_neighbourhood',
            new_name='neighbourhood',
        ),
    ]
