from django.urls import path

from information.api.views import CommentAPI, NewsAPI, PartnerAPI, ProductAPI, SlidersAPI

urlpatterns = [
    path('comment/', CommentAPI.as_view()),
    path('news/', NewsAPI.as_view()),
    path('partner/', PartnerAPI.as_view()),
    path('product/', ProductAPI.as_view()),
    path('slider/', SlidersAPI.as_view()),
]
