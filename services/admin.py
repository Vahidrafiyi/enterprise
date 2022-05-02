from django.contrib import admin
from django.contrib.admin import register

from services.models import Project, Service


@register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title_fa', 'start_time_fa', 'doing_time_fa', 'end_time_fa')


@register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_fa',)
