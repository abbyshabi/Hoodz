# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 13:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20190323_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='join',
        ),
    ]
