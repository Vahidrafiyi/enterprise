from django.contrib import admin
from django.contrib.admin import register

from header_footer.models import Footer, Header


@register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone')

@register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('parent', 'child')
