from django.db import models

# Create your models here.
class Feedback(models.Model):
    SOLVED = 'SL'
    REJECTED = 'RJ'
    DEFAULT = 'DF'
    IN_PROCESS = 'PR'
    STATUS_CHOICES = (
        (SOLVED, 'Решено'),
        (REJECTED, 'Не решено'),
        (DEFAULT, 'Не требует решения'),
        (IN_PROCESS, 'В процессе')
    )

    sender = models.CharField(max_length=50, verbose_name='Отправитель')
    text = models.TextField(verbose_name='Отзыв')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=IN_PROCESS, verbose_name='Статус')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return "%s - %s" % (self.sender, self.text[:20])
