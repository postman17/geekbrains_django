from django.urls import path
from product.views import view_products, details, add_product

app_name = 'product'
urlpatterns = [
    path('', view_products, name='index'),
    path('add', add_product, name='add'),
    path('detail/<str:product_name>/<str:product_content>/<path:product_image>', details, name='detail'),
]