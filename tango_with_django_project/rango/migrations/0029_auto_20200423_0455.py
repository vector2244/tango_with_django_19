# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2020-04-23 04:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0028_remove_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='rango.Category'),
        ),
    ]