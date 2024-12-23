from django.contrib import admin
from .models import Category, Product, CartItem, Cart

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
