from django.db import models
from django.utils.translation import ugettext_lazy as _


class Feedback(models.Model):
    DEFAULT = 'DF'
    IN_PROCESS = 'PR'
    NEW = 'NW'
    SOLVED = 'SL'
    REJECTED = 'RJ'
    STATUS_CHOICES = (
        (DEFAULT, "Don't need to be solved"),
        (IN_PROCESS, _('In progress')),
        (NEW, _('New')),
        (SOLVED, _('Solved')),
        (REJECTED, _("Won't be solved")),
    )

    sender = models.CharField(_('Sender'), max_length=50)
    text = models.TextField(_('Text'))
    created_at = models.DateField(_('Created at'), auto_now_add=True)
    status = models.CharField(_('Status'), max_length=2, choices=STATUS_CHOICES, default=NEW)

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')
        ordering = ('-created_at', )

    def __str__(self):
        return f'{self.sender} {self.text[:20]}'
