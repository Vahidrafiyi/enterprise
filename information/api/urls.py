from django.urls import path, re_path

from information.api.views import CommentAPI, NewsAPI, PartnerAPI, ProductAPI, SliderAPI,\
    AdminNewsAPI, AdminSliderAPI, AdminCommentAPI, AdminPartnerAPI, AdminProductAPI

urlpatterns = [
    # user
    path('comment/', CommentAPI.as_view()),
    path('news/', NewsAPI.as_view()),
    path('partner/', PartnerAPI.as_view()),
    path('product/', ProductAPI.as_view()),
    path('slider/', SliderAPI.as_view()),
    # admin
    re_path(r'admin/comment/$', AdminCommentAPI.as_view()),
    re_path(r'admin/comment/(?P<pk>[0-9]+)$', AdminCommentAPI.as_view()),
    re_path(r'admin/news/$', AdminNewsAPI.as_view()),
    re_path(r'admin/news/(?P<pk>[0-9]+)$', AdminNewsAPI.as_view()),
    re_path(r'admin/partner/$', AdminPartnerAPI.as_view()),
    re_path(r'admin/partner/(?P<pk>[0-9]+)$', AdminPartnerAPI.as_view()),
    re_path(r'admin/product/$', AdminProductAPI.as_view()),
    re_path(r'admin/product/(?P<pk>[0-9]+)$', AdminProductAPI.as_view()),
    re_path(r'admin/slider/$', AdminSliderAPI.as_view()),
    re_path(r'admin/slider/(?P<pk>[0-9]+)$', AdminSliderAPI.as_view()),
]
