# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-20 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_pages', '0004_auto_20190320_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='tour_date',
            field=models.CharField(max_length=150),
        ),
    ]