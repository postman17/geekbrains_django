from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('', index),
    path('contacts', contacts),
    path('about', about),
]