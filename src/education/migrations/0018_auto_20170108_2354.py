# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0017_auto_20170108_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eduprogram',
            name='url',
            field=models.SlugField(unique=True, verbose_name='Страница образовательной программы'),
        ),
    ]