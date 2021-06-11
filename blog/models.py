from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=160, verbose_name="Название")
    url = models.SlugField(max_length=255, unique=True, verbose_name="Ссылка")

    def __str__(self):
        return self.title
