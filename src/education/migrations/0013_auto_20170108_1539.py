# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0012_auto_20170108_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eduprogram',
            name='url',
            field=models.CharField(max_length=200, unique=True, verbose_name='Страница образовательной программы'),
        ),
    ]
