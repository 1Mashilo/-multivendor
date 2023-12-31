# vendor/urls.py
from django.urls import path
from .views import index
from .views import product_list

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product_list'),
]
