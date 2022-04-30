from django.contrib import admin
from django.contrib.admin import register

from accounts.models import Profile


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'created_at')
