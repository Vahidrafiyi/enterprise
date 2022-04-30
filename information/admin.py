from django.contrib import admin
from django.contrib.admin import register

from information.models import News, Comment, Product, Partner, Slider


@register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title',)


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)


@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('image', 'alt')


@register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
