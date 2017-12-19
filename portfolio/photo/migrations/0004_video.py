# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-11 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20171210_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('lien', models.CharField(max_length=100)),
                ('date_video', models.DateTimeField(null=True, verbose_name='Date de la vidéo')),
                ('date_ajout', models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
    ]
