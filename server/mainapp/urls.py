from django.urls import path
from mainapp.views import *

app_name = 'mainapp'
urlpatterns = [
    path('', index, name='index'),
    path('contacts', contacts, name='contacts'),
    path('about', about, name='about'),
]