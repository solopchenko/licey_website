# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_auto_20170106_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='educourse',
            name='full_description',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='educourse',
            name='description',
            field=models.CharField(blank=True, max_length=500, verbose_name='Краткое описание'),
        ),
    ]
