# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_document_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentSubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
