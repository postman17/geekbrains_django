from django.urls import path
from accounts.views import accounts_login

app_name = 'accounts'
urlpatterns = [
    path('', accounts_login, name='login'),
]