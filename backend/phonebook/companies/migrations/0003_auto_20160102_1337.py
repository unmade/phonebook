# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20151228_1029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='center',
            options={'ordering': ['number', 'name'], 'verbose_name': 'Центр', 'verbose_name_plural': 'Центры'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name': 'Предприятие', 'verbose_name_plural': 'Предприятия'},
        ),
        migrations.AlterModelOptions(
            name='companycategory',
            options={'ordering': ['category'], 'verbose_name': 'Тип предприятие', 'verbose_name_plural': 'Типы предприятий'},
        ),
        migrations.AlterModelOptions(
            name='division',
            options={'ordering': ['number', 'name'], 'verbose_name': 'Отделение/Отдел', 'verbose_name_plural': 'Отделения/Отделы'},
        ),
        migrations.AlterField(
            model_name='center',
            name='comment',
            field=models.CharField(blank=True, max_length=255, verbose_name='Доп. инф.'),
        ),
        migrations.AlterField(
            model_name='center',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company', verbose_name='Предприятие'),
        ),
        migrations.AlterField(
            model_name='center',
            name='emails',
            field=models.ManyToManyField(blank=True, to='contacts.Email', verbose_name='Эл. адреса'),
        ),
        migrations.AlterField(
            model_name='center',
            name='head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='center_head', to='employees.Employee', verbose_name='Начальник'),
        ),
        migrations.AlterField(
            model_name='center',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='center',
            name='number',
            field=models.CharField(max_length=10, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='center',
            name='phones',
            field=models.ManyToManyField(blank=True, to='contacts.Phone', verbose_name='Телефоны'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=400, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='company',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.CompanyCategory', verbose_name='Тип предприятия'),
        ),
        migrations.AlterField(
            model_name='company',
            name='ceo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_ceo', to='employees.Employee', verbose_name='Руководитель'),
        ),
        migrations.AlterField(
            model_name='company',
            name='comment',
            field=models.CharField(blank=True, max_length=255, verbose_name='Доп. инф.'),
        ),
        migrations.AlterField(
            model_name='company',
            name='emails',
            field=models.ManyToManyField(blank=True, to='contacts.Email', verbose_name='Эл. адреса'),
        ),
        migrations.AlterField(
            model_name='company',
            name='full_name',
            field=models.TextField(verbose_name='Полное название'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='logos/no-logo.png', upload_to='logos', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phones',
            field=models.ManyToManyField(blank=True, to='contacts.Phone', verbose_name='Телефоны'),
        ),
        migrations.AlterField(
            model_name='company',
            name='short_name',
            field=models.CharField(max_length=255, verbose_name='Сокращенное название'),
        ),
        migrations.AlterField(
            model_name='companycategory',
            name='category',
            field=models.CharField(max_length=50, unique=True, verbose_name='Аббревиатура'),
        ),
        migrations.AlterField(
            model_name='companycategory',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Полное название'),
        ),
        migrations.AlterField(
            model_name='division',
            name='center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Center', verbose_name='Центр'),
        ),
        migrations.AlterField(
            model_name='division',
            name='emails',
            field=models.ManyToManyField(blank=True, to='contacts.Email', verbose_name='Эл. адреса'),
        ),
        migrations.AlterField(
            model_name='division',
            name='head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='division_head', to='employees.Employee', verbose_name='Начальник'),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='division',
            name='number',
            field=models.CharField(max_length=10, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='division',
            name='phones',
            field=models.ManyToManyField(blank=True, to='contacts.Phone', verbose_name='Телефоны'),
        ),
    ]
