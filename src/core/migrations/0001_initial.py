# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500, verbose_name='Наименование меню')),
                ('href', models.CharField(blank=True, max_length=200, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name_plural': 'Меню',
                'verbose_name': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='MenuLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500, verbose_name='Наименование')),
                ('href', models.CharField(max_length=200, verbose_name='Ссылка')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Menu', verbose_name='Меню')),
            ],
            options={
                'verbose_name_plural': 'Ссылки в меню',
                'verbose_name': 'Ссылка в меню',
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('full_name', models.CharField(max_length=500, verbose_name='Полное наименование')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
                ('website', models.URLField(verbose_name='Сайт')),
                ('foundation_date', models.DateField(verbose_name='Дата ввода в эксплуатацию')),
                ('registration_date', models.DateField(verbose_name='Дата государственной регистрации')),
                ('accreditation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='docs.Document', verbose_name='Акредитация')),
            ],
            options={
                'verbose_name_plural': 'Информация об организации',
                'verbose_name': 'Информация об организации',
            },
        ),
        migrations.CreateModel(
            name='OrganisationBuilding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500, verbose_name='Наименование здания')),
                ('address', models.CharField(max_length=500, verbose_name='Адрес')),
                ('phone', models.CharField(blank=True, max_length=25, verbose_name='Телефон')),
                ('business_hours', models.TextField(max_length=500, verbose_name='Часы работы')),
                ('visiting_hours', models.TextField(blank=True, max_length=500, verbose_name='Часы приема')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Organisation')),
            ],
            options={
                'verbose_name_plural': 'Филиалы',
                'verbose_name': 'Филиал',
            },
        ),
        migrations.CreateModel(
            name='OrganisationFounder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500, verbose_name='Наименование организации')),
                ('head', models.CharField(max_length=500, verbose_name='Руководитель')),
                ('phone', models.CharField(max_length=25, verbose_name='Телефон')),
                ('address', models.CharField(max_length=500, verbose_name='Адрес')),
                ('business_hours', models.TextField(max_length=500, verbose_name='Часы работы')),
                ('visiting_hours', models.TextField(blank=True, max_length=500, verbose_name='Часы приема')),
                ('website', models.URLField(blank=True, verbose_name='Сайт')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Адрес электронной почты')),
                ('feedback', models.URLField(blank=True, verbose_name='Электронная приёмная')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Organisation')),
            ],
            options={
                'verbose_name_plural': 'Учредители',
                'verbose_name': 'Учредитель',
            },
        ),
    ]