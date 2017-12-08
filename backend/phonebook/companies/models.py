from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class CompanyManager(models.Manager):
    def get_queryset(self):
        queryset = super(CompanyManager, self).get_queryset()
        return queryset.select_related('ceo__surname', 'ceo__firstname', 'ceo__patronymic', 'ceo__position')\
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


class CompanyCategory(models.Model):  # TODO: rename to BusinessEntity
    category = models.CharField(_('Abbreviation'), max_length=50, unique=True)  # TODO: rename to abbreviation
    name = models.CharField(_('Name'), max_length=500)

    class Meta:
        verbose_name = _('Business entity')
        verbose_name_plural = _('Business entities')
        ordering = ['category']

    def __str__(self):
        return self.category


class Company(models.Model):
    ceo = models.ForeignKey(
        'employees.Employee', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='company_ceo', verbose_name=_('CEO')
    )
    category = models.ForeignKey(
        'CompanyCategory', null=True, blank=True, verbose_name=_('Business entity'), on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    full_name = models.TextField(_('Full name'), blank=True)
    short_name = models.CharField(_('Short name'), max_length=255, blank=True)
    address = models.CharField(_('Address'), max_length=400, blank=True)
    phones = models.ManyToManyField('contacts.Phone', blank=True, verbose_name=_('Phones'))
    emails = models.ManyToManyField('contacts.Email', blank=True, verbose_name=_('Emails'))
    logo = models.ImageField(_('Logo'), upload_to='logos', default='logos/no-logo.png', blank=True)
    comment = models.CharField(_('Additional info'), max_length=255, blank=True)
    objects = models.Manager()
    related_objects = CompanyManager()

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_api_url(self):
        return reverse('companies:api:company-detail', kwargs={'pk': self.pk})


class Center(models.Model):
    company = models.ForeignKey('Company', verbose_name=_('Company'), on_delete=models.CASCADE)
    head = models.ForeignKey(
        'employees.Employee', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='center_head', verbose_name=_('Head')
    )
    number = models.CharField(_('Code'), max_length=10)  # TODO: rename to Code
    name = models.CharField(_('Name'), max_length=255)
    comment = models.CharField(_('Additional info'), max_length=255, blank=True)
    phones = models.ManyToManyField('contacts.Phone', blank=True, verbose_name=_('Phones'))
    emails = models.ManyToManyField('contacts.Email', blank=True, verbose_name=_('Emails'))
    objects = models.Manager()
    related_objects = CenterManager()

    class Meta:
        verbose_name = _('Center')
        verbose_name_plural = _('Centers')
        ordering = ['number', 'name']

    def __str__(self):
        return f'{self.number} - {self.name}'

    def get_absolute_api_url(self):
        return reverse('companies:api:center-detail', kwargs={'pk': self.pk})


class Division(models.Model):
    center = models.ForeignKey('Center', verbose_name=_('Center'), on_delete=models.CASCADE)
    head = models.ForeignKey(
        'employees.Employee', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='division_head', verbose_name=_('Head')
    )
    number = models.CharField(_('Code'), max_length=10)  # TODO: rename to Code
    name = models.CharField(_('Name'), max_length=255, blank=True)
    comment = models.CharField(_('Additional info'), max_length=255, blank=True)
    phones = models.ManyToManyField('contacts.Phone', blank=True, verbose_name=_('Phones'))
    emails = models.ManyToManyField('contacts.Email', blank=True, verbose_name=_('Emails'))
    objects = models.Manager()
    related_objects = DivisionManager()

    class Meta:
        verbose_name = _('Division')
        verbose_name_plural = _('Divisions')
        ordering = ['number', 'name']

    def __str__(self):
        return f'{self.number} - {self.name}'

    def get_absolute_api_url(self):
        return reverse('companies:api:division-detail', kwargs={'pk': self.pk})
