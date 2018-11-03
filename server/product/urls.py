from django.urls import path
from .views import view_products, details, add_product, update_product, delete_product, category_list, category_detail

app_name = 'product'
urlpatterns = [
    path('', view_products, name='index'),
    path('categories', category_list, name='category_list'),
    path('categories/<int:pk>', category_detail, name='detail'),
    path('add', add_product, name='add'),
    path('<int:pk>/update', update_product, name='update'),
    path('<int:pk>/delete', delete_product, name='delete'),
    path('detail/<int:pk>', details, name='detail'),
]