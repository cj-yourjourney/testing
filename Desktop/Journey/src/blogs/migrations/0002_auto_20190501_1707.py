# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-01 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=False, unique=True),
        ),
    ]
