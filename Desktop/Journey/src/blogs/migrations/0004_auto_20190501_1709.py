# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-01 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20190501_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
