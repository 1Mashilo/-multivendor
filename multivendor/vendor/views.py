# views.py
from django.shortcuts import render, get_object_or_404, redirect,reverse
from .models import Product
from django.contrib.auth import login, authenticate
from .forms import ProductForm, UserRegistrationForm

def index(request):
    return render(request, 'vendor/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            
            # Log the user in after registration
            login(request, user)

            # Redirect to a success page or dashboard
            return redirect('dashboard')  # Adjust the URL name accordingly
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


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
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'vendor/add_product.html', {'form': form})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'vendor/edit_product.html', {'form': form, 'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'vendor/delete_product.html', {'product': product})

def dashboard(request):
    product_list_url = reverse('product_list')
    add_product_url = reverse('add_product')

    products = Product.objects.all()

    return render(request, 'vendor/dashboard.html', {'products': products, 'product_list_url': product_list_url, 'add_product_url': add_product_url})
