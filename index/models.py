from django.db import models


# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=180, verbose_name="Название слайда")
    alt = models.CharField(max_length=180, verbose_name="Сео заголовок")
    image = models.ImageField(upload_to="slider/", height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

    def __str__(self):
        return self.title    
    