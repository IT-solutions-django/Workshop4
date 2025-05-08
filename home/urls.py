from django.urls import path
from .views import *


app_name = 'home'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('home1/', Home1View.as_view(), name='home1'),
    path('home2/', Home2View.as_view(), name='home2'),
    path('home3/', Home3View.as_view(), name='home3'),
]