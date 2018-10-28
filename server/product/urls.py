from django.urls import path
from product.views import view_products, details

app_name = 'product'
urlpatterns = [
    path('', view_products, name='index'),
    path('detail/<str:product_name>/<str:product_content>', details, name='detail'),
]