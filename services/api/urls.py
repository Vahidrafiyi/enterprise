from django.urls import path, re_path

from services.api.views import ServiceAPI, ProjectAPI, AdminServiceAPI, AdminProjectAPI

urlpatterns = [
    # user
    path('service/', ServiceAPI.as_view()),
    path('project/', ProjectAPI.as_view()),
    # admin
    re_path(r'admin/service/$', AdminServiceAPI.as_view()),
    re_path(r'admin/service/(?P<pk>[0-9]+)$', AdminServiceAPI.as_view()),
    re_path(r'admin/project/$', AdminProjectAPI.as_view()),
    re_path(r'admin/project/(?P<pk>[0-9]+)$', AdminProjectAPI.as_view()),
]
