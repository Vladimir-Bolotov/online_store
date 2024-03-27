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
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Дата последнего изменения", auto_now=True)

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


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    slug = models.CharField(max_length=150, verbose_name="slug")
    content = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(verbose_name="Изображение")
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    is_published = models.BooleanField(verbose_name="Опубликовано")
    count_views = models.IntegerField(verbose_name="Просмотры", default=0)

    def __str__(self):
        return f"{self.title, self.count_views}"

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
