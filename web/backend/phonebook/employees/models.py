from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class FirstName(models.Model):
    name = models.CharField(_('First name'), max_length=50, unique=True)

    class Meta:
        verbose_name = _('First name')
        verbose_name_plural = _('First names')
        ordering = ['name']

    def __str__(self):
        return self.name


class Patronymic(models.Model):
    name = models.CharField(_('Patronymic'), max_length=50, unique=True)

    class Meta:
        verbose_name = _('Patronymic')
        verbose_name_plural = _('Patronymics')
        ordering = ['name']

    def __str__(self):
        return self.name


class Surname(models.Model):
    name = models.CharField(_('Surname'), max_length=50, unique=True)

    class Meta:
        verbose_name = _('Surname')
        verbose_name_plural = _('Surnames')
        ordering = ['name']

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(_('Name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('Position')
        verbose_name_plural = _('Positions')
        ordering = ['name']

    def __str__(self):
        return self.name


class EmployeeQuerySet(models.QuerySet):

    def select_name(self):
        return self.select_related('firstname', 'patronymic', 'surname')

    def select_job(self):
        return self.select_related('company', 'center', 'division', 'position')

    def prefetch_contacts(self):
        return self.prefetch_related('phones', 'emails', 'phones__category', 'emails__category')

    def prefetch_secretaries(self):
        return self.prefetch_related('secretaries')


class Employee(models.Model):
    surname = models.ForeignKey(
        'Surname', null=True, blank=True, verbose_name=_('Surname'), on_delete=models.SET_NULL
    )
    firstname = models.ForeignKey(
        'FirstName', null=True, blank=True, verbose_name=_('First name'), on_delete=models.SET_NULL
    )
    patronymic = models.ForeignKey(
        'Patronymic', null=True, blank=True, verbose_name=_('Patronymic'), on_delete=models.SET_NULL
    )

    birthday = models.DateField(_('Birthday'), null=True, blank=True)

    company = models.ForeignKey(
        'companies.Company', null=True, blank=True, verbose_name=_('Company'), on_delete=models.SET_NULL
    )
    center = models.ForeignKey(
        'companies.Center', null=True, blank=True, verbose_name=_('Center'), on_delete=models.SET_NULL
    )
    division = models.ForeignKey(
        'companies.Division', null=True, blank=True, verbose_name=_('Division'), on_delete=models.SET_NULL
    )
    position = models.ForeignKey(
        'Position', null=True, blank=True, verbose_name=_('Position'), on_delete=models.SET_NULL
    )
    boss = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='secretaries', verbose_name=_('Boss')
    )
    place = models.CharField(_('Place'), max_length=255, blank=True)

    comment = models.CharField(_('Additional info'), max_length=255, blank=True)
    phones = models.ManyToManyField('contacts.Phone', blank=True, verbose_name=_('Phones'))
    emails = models.ManyToManyField('contacts.Email', blank=True, verbose_name=_('Emails'))
    is_retired = models.BooleanField(_('Is retired'), default=False)
    objects = EmployeeQuerySet.as_manager()

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ['surname', 'firstname', 'patronymic']

    def __str__(self):
        return f'{self.surname} {self.firstname} {self.patronymic}'

    def get_absolute_api_url(self):
        return reverse('employees:api:employee-detail', kwargs={'pk': self.pk})
