from django.urls import path
from .views import *


app_name = 'blog'


urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('article/', ArticleView.as_view(), name='article')
]