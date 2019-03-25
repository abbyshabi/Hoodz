# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 15:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0008_remove_business_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_image_url', models.ImageField(upload_to='images/')),
                ('neigh_name', models.CharField(max_length=30)),
                ('neigh_description', models.TextField(max_length=100)),
                ('neigh_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('location', models.CharField(max_length=30)),
                ('occupants', models.IntegerField(default=0)),
                ('neigh_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neigh', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]