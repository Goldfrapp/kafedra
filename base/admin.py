from django.contrib import admin
from .models import Base


class BaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'active', 'slug', 'created', 'published']
    fieldsets = (
        (None,  {
            'fields': ('title', 'active', 'position', 'created', 'published')
        }),
        ('Сео', {
            'fields': ('slug', 'meta_title', 'meta_description', 'meta_keywords', 'h1')
        }),
        ('Контент', {
            'fields': ('boss', 'address', 'phone', 'mail', 'image', 'intro_text', 'text')
        }),
    )
    list_display_links = ['title', 'slug']
    list_filter = ['active', 'created', 'published']
    search_fields = ['title', 'meta_description', 'meta_keywords', 'slug', 'text', 'h1', 'meta_title', 'boss',
                     'address', 'phone', 'mail']


admin.site.register(Base, BaseAdmin)
