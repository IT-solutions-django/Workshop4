from django.urls import path
from .views import *


app_name = 'blog'


urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('<int:category_id>/', BlogCategoryView.as_view(), name='blog_category'),
    path('article/<slug:slug>/', ArticleView.as_view(), name='article')
]