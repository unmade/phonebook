from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Email(models.Model):
    email = models.EmailField(unique=True, verbose_name='Эл. адрес')
    category = models.ForeignKey('Category', verbose_name='Категория')
    comment = models.CharField(max_length=255, blank=True, verbose_name='Доп. инф.')

    class Meta:
        verbose_name = 'Электронный адрес'
        verbose_name_plural = 'Электронные адреса'
        ordering = ['email']

    def __str__(self):
        return self.email


class Phone(models.Model):
    number = models.CharField(max_length=20, unique=True, verbose_name='Номер')
    category = models.ForeignKey('Category', verbose_name='Категория')
    comment = models.CharField(max_length=255, blank=True, verbose_name='Доп. инф.')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        ordering = ['number']

    def __str__(self):
        return self.number
