# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2020-04-18 18:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0024_auto_20200418_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
