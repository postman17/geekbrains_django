from django.urls import path
from accounts.views import accounts_login, accounts_register

app_name = 'accounts'

urlpatterns = [
    path('', accounts_login, name='login'),
    path('register', accounts_register, name='register'),
]