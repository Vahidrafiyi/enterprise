from django.contrib import admin
from django.contrib.admin import register

from article.models import Article


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
