# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_documentcategory_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]
