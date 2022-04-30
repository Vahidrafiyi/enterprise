from django.urls import re_path

from article.api.views import ArticleAPI, ArticlesGroupAPI

urlpatterns = [
    re_path(r'article/(?P<pk>[0-9]*)', ArticleAPI.as_view()),
    re_path(r'group/(?P<pk>[0-9]*)', ArticlesGroupAPI.as_view())
]
