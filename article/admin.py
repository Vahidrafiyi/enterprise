from django.contrib import admin
from django.contrib.admin import register

from article.models import Article, ArticleGroup


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')

@register(ArticleGroup)
class ArticleGroupAdmin(admin.ModelAdmin):
    list_display = ('title',)
