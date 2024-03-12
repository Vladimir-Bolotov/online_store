from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(**NULLABLE, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(verbose_name="Дата создания")
    updated_at = models.DateField(verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.name, self.price}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Contact(models.Model):
    country = models.CharField(max_length=100, verbose_name="Страна")
    inn = models.CharField(max_length=15, verbose_name="ИНН")
    address = models.CharField(max_length=250, verbose_name="Адрес")

    def __str__(self):
        return f'{self.country, self.inn, self.address}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
