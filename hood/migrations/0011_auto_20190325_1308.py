# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0010_auto_20190325_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='neigh_admin',
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='neighbour_hood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Project'),
        ),
        migrations.DeleteModel(
            name='Neighbourhood',
        ),
    ]
