from django.urls import path

from product.views import ProductJsonListView


app_name = 'rest_products'

urlpatterns = [
    path('', ProductJsonListView.as_view(), name='list'),
]
