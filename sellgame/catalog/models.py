from django.db import models
from datetime import datetime
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', ]

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',  args=[self.slug])
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.TextField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to="game/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    price = models.FloatField(verbose_name='Цена')
    stock = models.IntegerField(verbose_name='Осталось')
    Publisher = models.TextField(verbose_name='Издатель')
    Developer = models.TextField(verbose_name='Разработчик')
    release = models.DateField(verbose_name="Дата выхода")
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'
        ordering = ['name', 'time_create']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
