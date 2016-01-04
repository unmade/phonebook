# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=models.CharField(choices=[('SLVD', 'Решено'), ('RJCT', 'Не решено'), ('DFLT', 'Не требует решения'), ('PRCS', 'В процессе')], default='PRCS', max_length=2, verbose_name='Статус'),
        ),
    ]
