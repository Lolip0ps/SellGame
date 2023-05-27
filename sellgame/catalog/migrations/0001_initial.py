# Generated by Django 4.2.1 on 2023-05-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='game/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('Publisher', models.TextField(verbose_name='Издатель')),
                ('Developer', models.TextField(verbose_name='Разработчик')),
                ('release', models.DateField(verbose_name='Дата выхода')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталог',
                'ordering': ['name', 'time_create'],
            },
        ),
    ]
