from django.urls import path
from .views import ProductCreate, ProductUpdate, ProductDelete, ProductList, ProductDetail, CategoryList, CategoryDetail

app_name = 'product'
urlpatterns = [
    path('', ProductList.as_view(), name='index'),
    path('categories', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
    path('add', ProductCreate.as_view(), name='add'),
    path('<int:pk>/update', ProductUpdate.as_view(), name='update'),
    path('<int:pk>/delete', ProductDelete.as_view(), name='delete'),
    path('detail/<int:pk>', ProductDetail.as_view(), name='detail'),
]