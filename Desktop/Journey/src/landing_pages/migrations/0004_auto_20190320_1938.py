# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-20 19:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_pages', '0003_auto_20190320_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='tour_time',
            new_name='tour_date',
        ),
    ]
