from django.urls import path
from .views import *


app_name = 'contacts'


urlpatterns = [
    path('company/', AboutCompanyView.as_view(), name='about_company'),

    path('api/save-request/', SaveRequestView.as_view(), name='save_request'),
]