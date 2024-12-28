from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    stock_qty = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)
    image = models.ImageField(upload_to='products/', default='default.jpg')

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    qty = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_items')


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

