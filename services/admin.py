from django.contrib import admin
from django.contrib.admin import register

from services.models import Project, Service


@register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'doing_time', 'end_time')


@register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
