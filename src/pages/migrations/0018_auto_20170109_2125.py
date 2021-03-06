# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20170109_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(max_length=100, verbose_name='URL'),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('parent', 'slug')]),
        ),
    ]
