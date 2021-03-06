# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0011_auto_20170108_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eduprogram',
            name='description',
            field=models.CharField(blank=True, help_text='Краткое описание, например, автор программы.', max_length=200, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='url',
            field=models.CharField(blank=True, max_length=200, unique=True, verbose_name='Страница образовательной программы'),
        ),
    ]
