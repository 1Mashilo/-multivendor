# views.py
from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    return render(request, 'vendor/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'vendor/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'vendor/product_detail.html', {'product': product})
