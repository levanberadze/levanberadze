from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category, Cart, CartItem
from .forms import ProductForm
from django.contrib import messages



def home(request):
    product_name = request.GET.get('product_name')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category = request.GET.get('category')
    in_stock = request.GET.get('in_stock')

    filters = dict()


    if product_name:
        filters['name__icontains'] = product_name

    if min_price:
        filters['price__gt'] = min_price

    if max_price:
        filters['price__lt'] = max_price

    if in_stock == 'on':
        filters['stock_qty__gt'] = 0

    if category:
        filters['category'] = category

    products = Product.objects.filter(**filters)

    paginator_obj = Paginator(products, 2)

    page_number = request.GET.get('page')
    try:
        products = paginator_obj.get_page(page_number)
    except PageNotAnInteger:
        products = paginator_obj.page(1)
    except EmptyPage:
        products = paginator_obj.page(paginator_obj.num_pages)



    categories = Category.objects.all()

    return render(request, 'home.html', {'products': products, 'categories': categories})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})


def create_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'product_form.html', {'form': form})


def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Product {product.name} Has Been Updated Successfully')
            return redirect('product_detail', id=id)
    return render(request, 'product_form.html', {'form': form, 'product': product})


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, f'Product {product.name} Has Been Deleted Successfully')
        return redirect('home')


def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', context={'cart': cart})


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart_item = CartItem.objects.create(product=product, cart=request.user.cart)
    return redirect('product_detail', id=id)