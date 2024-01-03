# urls.py
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('success/',views.payment_success_view,name='success'),
    path('failed/',views.payment_failed_view,name='failed'),
    path('api/checkout-session/<int:pk>/',views.create_checkout_session,name='api_checkout_session'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('addproduct/', views.add_product, name='add_product'),
    path('editproduct/<int:pk>/', views.edit_product, name='edit_product'),
    path('deleteproduct/<int:pk>/', views.delete_product, name='delete_product'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('invalid/', views.invalid, name='invalid'),
    path('purchases/', views.my_purchases, name='my_purchases'),
    path('sales/',views.sales,name='sales'),
]


