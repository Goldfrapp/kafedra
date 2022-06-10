from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Base(models.Model):
    class Meta:
        verbose_name = 'Учебная база'
        verbose_name_plural = 'Учебные базы'

    title = models.CharField(max_length=255, blank=True, verbose_name='Название базы')
    active = models.BooleanField(default=True, verbose_name='Активировать')
    meta_title = models.CharField(max_length=120, blank=True, verbose_name="Мета-заголовок",
                                  help_text='Заголовок для поисковиков')
    h1 = models.CharField(max_length=120, blank=True, verbose_name='H1 заголовок',
                          help_text='H1 заголовок для поисковиков')
    meta_description = models.CharField(max_length=180, blank=True, verbose_name='Мета-описание',
                                        help_text='Краткое описание базы для поисковиков')
    meta_keywords = models.TextField(blank=True, verbose_name='Ключевые слова')
    slug = models.SlugField(blank=True, unique=True, verbose_name='URL-ссылка',
                            help_text='Поле заполняется автоматически')
    position = models.PositiveSmallIntegerField(default=0, verbose_name='Позиция')
    boss = models.CharField(max_length=255, blank=True,verbose_name='ФИО руководителя')
    address = models.TextField(blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=100, blank=True, verbose_name='Телефон')
    mail = models.EmailField(blank=True, verbose_name='E-mail')
    image = models.ImageField(upload_to='base/', blank=True, verbose_name='Изображение')
    intro_text = models.TextField(blank=True, verbose_name='Превью')
    text = RichTextUploadingField(verbose_name="Описание", null=True, blank=True)
    tags = TaggableManager(blank=True, help_text='Теги')
    created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    published = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Base, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('base_detail_page', args=[str(self.slug)])
