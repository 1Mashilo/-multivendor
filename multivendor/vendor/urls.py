# urls.py
from django.urls import path
from .views import index, product_list, product_detail,add_product,edit_product,delete_product,dashboard, register,custom_login,custom_logout,invalid


urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:pk>/', edit_product, name='edit_product'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('invalid/', invalid, name='invalid'),
]

