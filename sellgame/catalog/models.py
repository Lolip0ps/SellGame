from django.db import models
from datetime import datetime
from django.urls import reverse


class Catalog(models.Model):
    name = models.TextField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to="game/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    price = models.FloatField(verbose_name='Цена')
    # platform = models.TextField(verbose_name='Платформа')
    Publisher = models.TextField(verbose_name='Издатель')
    Developer = models.TextField(verbose_name='Разработчик')
    release = models.DateField(verbose_name="Дата выхода")
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'
        ordering = ['name', 'time_create']
