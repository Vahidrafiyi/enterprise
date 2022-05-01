from django.urls import path, re_path

from accounts.api.views import CurrentUserProfileAPI, AdminProfileAPI

urlpatterns = [
    path('profile/', CurrentUserProfileAPI.as_view()),
    re_path(r'admin/profile/$', AdminProfileAPI.as_view()),
    re_path(r'admin/profile/(?P<pk>[0-9]+)$', AdminProfileAPI.as_view()),
]
