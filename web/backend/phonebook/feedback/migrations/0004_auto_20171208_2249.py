# Generated by Django 2.0 on 2017-12-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20171208_2003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ('-created_at',), 'verbose_name': 'Feedback', 'verbose_name_plural': 'Feedback'},
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='sender',
            field=models.CharField(max_length=50, verbose_name='Sender'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=models.CharField(choices=[('DF', "Don't need to be solved"), ('PR', 'In progress'), ('NW', 'New'), ('SL', 'Solved'), ('RJ', "Won't be solved")], default='NW', max_length=2, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
    ]