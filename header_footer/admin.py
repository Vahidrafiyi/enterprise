from django.contrib import admin
from django.contrib.admin import register

from header_footer.models import Footer, SocialMedia, Menu, Logo


@register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('address_fa', 'email', 'phone_fa')


@register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title_fa', 'parent')


@register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('logo_text_fa', 'logo_alt', 'logo_image')


@register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('image', 'alt')
