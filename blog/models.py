from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=160, verbose_name="Название")
    url = models.SlugField(max_length=255, unique=True, verbose_name="Ссылка")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание категории")
    image = models.ImageField(upload_to='blog/category', blank=True, verbose_name="Изображение")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title
