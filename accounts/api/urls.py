from django.urls import path

from accounts.api.views import CurrentUserProfileAPI

urlpatterns = [
    path('profile/', CurrentUserProfileAPI.as_view())
]
