from django.db import models

from companies.models import Company, Center, Division
from contacts.models import Email, Phone

# Create your models here.
class FirstName(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'

    def __str__(self):
        return self.name


class Patronymic(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Отчество'
        verbose_name_plural = 'Отчества'

    def __str__(self):
        return self.name


class Surname(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Фамилия')

    class Meta:
        verbose_name = 'Фамилия'
        verbose_name_plural = 'Фамилии'

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Employee(models.Model):
    surname = models.ForeignKey('Surname', null=True, blank=True, verbose_name='Фамилия')
    first_name = models.ForeignKey('FirstName', null=True, blank=True, verbose_name='Имя')
    patronymic = models.ForeignKey('Patronymic', null=True, blank=True, verbose_name='Отчество')
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    company = models.ForeignKey('companies.Company', null=True, blank=True, verbose_name='Предприятие')
    center = models.ForeignKey('companies.Center', null=True, blank=True, verbose_name='Центр')
    division = models.ForeignKey('companies.Division', null=True, blank=True, verbose_name='Отделение/Отдел')
    position = models.ForeignKey('Position', null=True, blank=True, verbose_name='Должность')
    place = models.CharField(max_length=255, blank=True, verbose_name='Рабочее место')
    comment = models.CharField(max_length=255, blank=True, verbose_name='Доп. инф.')
    phones = models.ManyToManyField('contacts.Phone', null=True, blank=True, verbose_name='Телефоны')
    emails = models.ManyToManyField('contacts.Email', null=True, blank=True, verbose_name='Эл. адреса')
    boss = models.ForeignKey('self', null=True, blank=True, related_name='secretary', verbose_name='Руководитель')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return "%s %s" % (self.surname, self.first_name)
