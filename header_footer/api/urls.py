from django.urls import path

from header_footer.api.views import FooterAPI, HeaderAPI, SocialMediaAPI

urlpatterns = [
    path('footer/', FooterAPI.as_view()),
    path('header/', HeaderAPI.as_view()),
    path('social-media/', SocialMediaAPI.as_view()),
]
