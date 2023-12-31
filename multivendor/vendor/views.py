# vendor/views.py
from django.shortcuts import render
from .models import Product

def index(request):
    return render(request, 'vendor/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'vendor/product_list.html', {'products': products})

