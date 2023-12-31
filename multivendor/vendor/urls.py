# urls.py
from django.urls import path
from .views import index, product_list, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
]
