from django.core.urlresolvers import reverse
from django.db import models

from contacts.models import Email, Phone

# Create your models here.
class CompanyManager(models.Manager):
    def get_queryset(self):
        queryset = super(CompanyManager, self).get_queryset()
        return queryset.select_related('ceo__surname', 'ceo__firstname', 'ceo__patronymic')\
                       .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')


class CenterManager(models.Manager):
    def get_queryset(self):
        queryset = super(CenterManager, self).get_queryset()
        return queryset.select_related('head', 'head__surname', 'head__firstname', 'head__patronymic')\
                       .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')


class DivisionManager(models.Manager):
    def get_queryset(self):
        queryset = super(DivisionManager, self).get_queryset()
        return queryset.select_related('head', 'head__surname', 'head__firstname', 'head__patronymic')\
                       .prefetch_related('phones', 'emails', 'phones__category', 'emails__category')


class CompanyCategory(models.Model):
    category = models.CharField(max_length=50, unique=True, verbose_name='Аббревиатура')
    name = models.CharField(max_length=500, verbose_name='Полное название')

    class Meta:
        verbose_name = "Тип предприятие"
        verbose_name_plural = "Типы предприятий"
        ordering = ['category']

    def __str__(self):
        return self.category


class Company(models.Model):
    ceo = models.ForeignKey('employees.Employee', null=True, blank=True, on_delete=models.SET_NULL,
                            related_name='company_ceo', verbose_name='Руководитель')
    category = models.ForeignKey('CompanyCategory', null=True, blank=True, verbose_name='Тип предприятия')
    name = models.CharField(max_length=255, verbose_name='Название')
    full_name = models.TextField(verbose_name='Полное название', blank=True)
    short_name = models.CharField(max_length=255, verbose_name='Сокращенное название', blank=True)
    address = models.CharField(max_length=400, verbose_name='Адрес', blank=True)
    phones = models.ManyToManyField('contacts.Phone', blank=True, verbose_name='Телефоны')
    emails = models.ManyToManyField('contacts.Email', blank=True, verbose_name='Эл. адреса')
    logo = models.ImageField(upload_to='logos', default='logos/no-logo.png', blank=True, verbose_name='Логотип')
    comment = models.CharField(max_length=255, blank=True, verbose_name='Доп. инф.')
    objects = models.Manager()
    related_objects = CompanyManager()

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"
        ordering = ['name']

    def get_absolute_api_url(self):
        return reverse('api:company-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Center(models.Model):
    company = models.ForeignKey('Company', verbose_name='Предприятие')
    head = models.ForeignKey('employees.Employee', null=True, blank=True, on_delete=models.SET_NULL,
                             related_name='center_head', verbose_name="Начальник")
    number = models.CharField(max_length=10, verbose_name='Номер')
    name = models.CharField(max_length=255, verbose_name='Название')
    comment = models.CharField(max_length=255, blank=True, verbose_name='Доп. инф.')
    phones = models.ManyToManyField('contacts.Phone', blank=True, verbose_name='Телефоны')
    emails = models.ManyToManyField('contacts.Email', blank=True, verbose_name='Эл. адреса')
    objects = models.Manager()
    related_objects = CenterManager()

    class Meta:
        verbose_name = 'Центр'
        verbose_name_plural = 'Центры'
        ordering = ['number', 'name']

    def get_absolute_api_url(self):
        return reverse('api:center-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s - %s" % (self.number, self.name)


class Division(models.Model):
    center = models.ForeignKey('Center', verbose_name='Центр')
    head = models.ForeignKey('employees.Employee', null=True, blank=True, on_delete=models.SET_NULL,
                             related_name='division_head', verbose_name='Начальник')
    number = models.CharField(max_length=10, verbose_name='Номер')
    name = models.CharField(max_length=255, blank=True, verbose_name='Название')
    comment = models.CharField(max_length=255, blank=True, verbose_name='Доп. инф.')
    phones = models.ManyToManyField('contacts.Phone', blank=True, verbose_name='Телефоны')
    emails = models.ManyToManyField('contacts.Email', blank=True, verbose_name='Эл. адреса')
    objects = models.Manager()
    related_objects = DivisionManager()

    class Meta:
        verbose_name = 'Отделение/Отдел'
        verbose_name_plural = 'Отделения/Отделы'
        ordering = ['number', 'name']

    def get_absolute_api_url(self):
        return reverse('api:division-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s - %s" % (self.number, self.name)
