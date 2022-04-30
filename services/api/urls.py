from django.urls import path

from services.api.views import ServiceAPI, ProjectAPI

urlpatterns = [
    path('service/', ServiceAPI.as_view()),
    path('project/', ProjectAPI.as_view()),
]
