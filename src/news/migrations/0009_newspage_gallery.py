# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
        ('news', '0008_auto_20161217_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery', verbose_name='Галерея'),
        ),
    ]
