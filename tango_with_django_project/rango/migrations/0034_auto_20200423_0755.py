# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2020-04-23 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0033_auto_20200423_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rango.Category'),
            preserve_default=False,
        ),
    ]