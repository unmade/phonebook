from django.db import models


# Create your models here.
class Feedback(models.Model):
    DEFAULT = 'DF'
    IN_PROCESS = 'PR'
    NEW = 'NW'
    SOLVED = 'SL'
    REJECTED = 'RJ'
    STATUS_CHOICES = (
        (DEFAULT, 'Не требует решения'),
        (IN_PROCESS, 'В процессе'),
        (NEW, 'Новое'),
        (SOLVED, 'Решено'),
        (REJECTED, 'Не решено'),
    )

    sender = models.CharField(max_length=50, verbose_name='Отправитель')
    text = models.TextField(verbose_name='Отзыв')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW, verbose_name='Статус')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-created_at', )

    def __str__(self):
        return "%s - %s" % (self.sender, self.text[:20])
