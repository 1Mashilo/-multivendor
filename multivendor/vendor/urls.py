# urls.py
from django.urls import path
from .views import index, product_list, product_detail,add_product

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('add_product/', add_product, name='add_product'),

]
