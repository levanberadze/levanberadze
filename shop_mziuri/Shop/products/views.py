from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_detail(request):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})