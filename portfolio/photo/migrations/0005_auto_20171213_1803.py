# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-13 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('envoyeur', models.EmailField(max_length=254)),
                ('date_envoi', models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='lien',
            field=models.URLField(max_length=100),
        ),
    ]