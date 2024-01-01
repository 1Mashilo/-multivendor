# views.py
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm

def index(request):
    return render(request, 'vendor/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'vendor/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'vendor/product_detail.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Assuming you have a URL pattern named 'product_list'
    else:
        form = ProductForm()

    return render(request, 'vendor/add_product.html', {'form': form})