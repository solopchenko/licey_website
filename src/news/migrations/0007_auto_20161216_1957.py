# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20161216_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff.Person', verbose_name='Автор'),
        ),
    ]