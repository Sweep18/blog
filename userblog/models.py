from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    date = models.DateTimeField(auto_now=True, verbose_name="Дата")
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(max_length=255, verbose_name='Текст')
    image = models.ImageField(upload_to='image', blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-date',)

    def __str__(self):
        return self.title


class CommentNews(models.Model):
    date = models.DateTimeField(auto_now=True, verbose_name="Дата")
    user = models.ForeignKey(User, verbose_name='Пользователь')
    news = models.ForeignKey(News, verbose_name='Новость')
    comment = models.TextField(max_length=255, verbose_name='Оставить комментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
