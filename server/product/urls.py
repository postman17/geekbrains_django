from django.urls import path
from .views import view_products, details, add_product, update_product, delete_product

app_name = 'product'
urlpatterns = [
    path('', view_products, name='index'),
    path('add', add_product, name='add'),
    path('<int:pk>/update', update_product, name='update'),
    path('<int:pk>/delete', delete_product, name='delete'),
    path('detail/<str:product_name>/<str:product_content>/<path:product_image>', details, name='detail'),
]