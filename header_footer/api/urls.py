from django.urls import path, re_path

from header_footer.api.views import FooterAPI, LogoAPI,MenuAPI, AdminSocialMediaAPI, AdminFooterAPI, AdminLogoAPI, AdminMenuAPI

urlpatterns = [
    #user
    path('footer/', FooterAPI.as_view()),
    path('header/', LogoAPI.as_view()),
    path('menu/', MenuAPI.as_view()),
    #admin
    re_path(r'admin/social-media/$', AdminSocialMediaAPI.as_view()),
    re_path(r'admin/social-media/(?P<pk>[0-9]+)$', AdminSocialMediaAPI.as_view()),
    re_path(r'admin/menu/$', AdminMenuAPI.as_view()),
    re_path(r'admin/menu/(?P<pk>[0-9]+)$', AdminMenuAPI.as_view()),
    re_path(r'admin/logo/$', AdminLogoAPI.as_view()),
    re_path(r'admin/logo/(?P<pk>[0-9]+)$', AdminLogoAPI.as_view()),
    re_path(r'admin/footer/$', AdminFooterAPI.as_view()),
    # re_path(r'admin/footer/(?P<pk>[0-9]+)$', AdminSocialMediaAPI.as_view()),
]
