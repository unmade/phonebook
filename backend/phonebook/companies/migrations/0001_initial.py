# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 10:29
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('comment', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('full_name', models.TextField()),
                ('short_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=400)),
                ('logo', models.ImageField(blank=True, default='logos/no-logo.png', upload_to='logos')),
                ('comment', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Center')),
                ('emails', models.ManyToManyField(blank=True, null=True, to='contacts.Email')),
            ],
        ),
    ]
