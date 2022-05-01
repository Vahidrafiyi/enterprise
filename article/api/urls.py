from django.urls import re_path

from article.api.views import ArticleAPI, ArticlesGroupAPI, AdminArticleAPI, AdminGroupAPI

urlpatterns = [
    # user
    re_path(r'article/(?P<pk>[0-9]*)$', ArticleAPI.as_view()),
    re_path(r'group/(?P<pk>[0-9]*)$', ArticlesGroupAPI.as_view()),
    # admin
    re_path(r'admin/article/$', AdminArticleAPI.as_view()),
    re_path(r'admin/article/(?P<pk>[0-9]+)$', AdminArticleAPI.as_view()),
    re_path(r'admin/group/$', AdminGroupAPI.as_view()),
    re_path(r'admin/group/(?P<pk>[0-9]+)$', AdminGroupAPI.as_view()),
]
