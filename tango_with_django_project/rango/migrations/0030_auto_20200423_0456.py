# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2020-04-23 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0029_auto_20200423_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Category'),
        ),
    ]