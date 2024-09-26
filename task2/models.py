from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок статьи')
    body = models.TextField(verbose_name='Текст статьи')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'