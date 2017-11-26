from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class FirstName(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'
        ordering = ['name']

    def __str__(self):
        return self.name


class Patronymic(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Отчество'
        verbose_name_plural = 'Отчества'
        ordering = ['name']

    def __str__(self):
        return self.name


class Surname(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Фамилия')

    class Meta:
        verbose_name = 'Фамилия'
        verbose_name_plural = 'Фамилии'
        ordering = ['name']

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['name']

    def __str__(self):
        return self.name


class EmployeeManager(models.Manager):
    def get_queryset(self):
        queryset = super(EmployeeManager, self).get_queryset()
        return queryset.select_related('firstname', 'patronymic', 'surname',
                                       'company', 'center', 'division', 'position')\
                       .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')


class Employee(models.Model):
    surname = models.ForeignKey('Surname', null=True, blank=True, verbose_name='Фамилия')
    firstname = models.ForeignKey('FirstName', null=True, blank=True, verbose_name='Имя')
    patronymic = models.ForeignKey('Patronymic', null=True, blank=True, verbose_name='Отчество')
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    company = models.ForeignKey('companies.Company', null=True, blank=True, verbose_name='Предприятие')
    center = models.ForeignKey('companies.Center', null=True, blank=True, verbose_name='Центр')
    division = models.ForeignKey('companies.Division', null=True, blank=True, verbose_name='Отделение/Отдел')
    position = models.ForeignKey('Position', null=True, blank=True, verbose_name='Должность')
    place = models.CharField(max_length=255, blank=True, verbose_name='Рабочее место')
    comment = models.CharField(max_length=255, blank=True, verbose_name='Доп. инф.')
    phones = models.ManyToManyField('contacts.Phone', blank=True, verbose_name='Телефоны')
    emails = models.ManyToManyField('contacts.Email', blank=True, verbose_name='Эл. адреса')
    boss = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                             related_name='secretary', verbose_name='Является секретарем у')
    is_retired = models.BooleanField(default=False, verbose_name="Числится уволеным")
    objects = models.Manager()
    related_objects = EmployeeManager()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['surname', 'firstname', 'patronymic']

    def get_absolute_api_url(self):
        return reverse('api:employees-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s %s %s" % (self.surname, self.firstname, self.patronymic)
