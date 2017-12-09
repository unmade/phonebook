# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 13:38
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20151228_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'ordering': ['email'], 'verbose_name': 'Электронный адрес', 'verbose_name_plural': 'Электронные адреса'},
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={'ordering': ['number'], 'verbose_name': 'Телефон', 'verbose_name_plural': 'Телефоны'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='email',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='email',
            name='comment',
            field=models.CharField(blank=True, max_length=255, verbose_name='Доп. инф.'),
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Эл. адрес'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='comment',
            field=models.CharField(blank=True, max_length=255, verbose_name='Доп. инф.'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(max_length=20, unique=True, verbose_name='Номер'),
        ),
    ]