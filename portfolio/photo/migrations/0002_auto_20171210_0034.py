# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-10 00:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='date_ajout',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de parution'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='date_photo',
            field=models.DateTimeField(null=True, verbose_name='Date de la photo'),
        ),
        migrations.AddField(
            model_name='photo',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]
