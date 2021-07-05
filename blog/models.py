from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категории блога'

    title = models.CharField(max_length=120, unique=True, blank=False, verbose_name='Название категории блога')
    active = models.BooleanField(default=True, verbose_name='Активировать')
    meta_title = models.CharField(max_length=120, blank=True, verbose_name="Мета-заголовок",
                                  help_text='Заголовок для поисковиков')
    h1 = models.CharField(max_length=120, blank=True, verbose_name='H1 заголовок',
                          help_text='H1 заголовок для поисковиков')
    meta_description = models.CharField(max_length=180, blank=True, verbose_name='Мета-описание',
                                        help_text='Краткое описание категории для поисковиков')
    meta_keywords = models.TextField(blank=True, verbose_name='Ключевые слова')
    slug = models.SlugField(blank=True, unique=True, verbose_name='URL-ссылка',
                            help_text='Поле заполняется автоматически')
    position = models.PositiveSmallIntegerField(default=0, verbose_name='Позиция')
    image = models.ImageField(upload_to='blog/category/', blank=True, verbose_name='Изображение')
    intro_text = models.TextField(blank=True, verbose_name='Превью')
    text = RichTextUploadingField(verbose_name="Описание", null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    published = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = RichTextUploadingField(verbose_name="Текст статьи", null=True, blank=True)
    image = models.ImageField(upload_to='blog/articles/', blank=True, verbose_name='Изображение')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(70, 70)], format='JPEG',
                                         options={'quality': 60})
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
