from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    body = models.TextField(verbose_name='Текст поста')
    # created = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=7, decimal_places=2)
    age = models.IntegerField()


class Game(models.Model):
    title = models.TextField()
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name="games")
