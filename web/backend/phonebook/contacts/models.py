from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=100, unique=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __str__(self):
        return self.name


class Email(models.Model):
    email = models.EmailField(_('Email'), unique=True)
    category = models.ForeignKey('Category', verbose_name=_('Category'), on_delete=models.CASCADE)
    comment = models.CharField(_('Additional info'), max_length=255, blank=True)

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')
        ordering = ['email']

    def __str__(self):
        return self.email


class Phone(models.Model):
    number = models.CharField(_('Number'), max_length=20, unique=True)
    category = models.ForeignKey('Category', verbose_name=_('Category'), on_delete=models.CASCADE)
    comment = models.CharField(_('Additional info'), max_length=255, blank=True)

    class Meta:
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')
        ordering = ['number']

    def __str__(self):
        return self.number
