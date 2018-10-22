from django.urls import path
from product.views import view_products, details

urlpatterns = [
    path('', view_products),
    path('detail/<str:product_name>/<str:product_content>', details),
]