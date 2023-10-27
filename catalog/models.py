from django.db import models
from django.utils.datetime_safe import date

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    img = models.ImageField(upload_to='category/', **NULLABLE, verbose_name='Изображение')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    img = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_begin = models.DateField(default=date.today, verbose_name='Дата создания')
    date_chang = models.DateField(default=date.today, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slag = models.CharField(max_length=150, verbose_name='Slag')
    text = models.TextField(verbose_name='Содержимое', **NULLABLE)
    img = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    date_begin = models.DateField(default=date.today, verbose_name='Дата создания')
    activate = models.BooleanField(default=True)
    count_views = models.IntegerField(verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'