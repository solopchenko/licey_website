# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20170109_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pages.Page', verbose_name='Родительская страница'),
        ),
    ]