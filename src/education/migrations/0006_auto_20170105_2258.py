# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_auto_20170105_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educourse',
            name='program',
        ),
        migrations.AddField(
            model_name='eduprogram',
            name='courses',
            field=models.ManyToManyField(blank=True, to='education.EduCourse', verbose_name='Дисциплины'),
        ),
    ]
