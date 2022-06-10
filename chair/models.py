from django.db import models


# Create your models here.
class teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя преподавателя', unique=True, null=False)

