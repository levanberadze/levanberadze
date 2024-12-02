from django.db import models
from django.forms import CharField


class Author(models.Model):
    name = models.CharField(max_length=100, null=True)



class Book(models.Model):
    BOOK_TYPES = {
        'detective': "Detective",
        'comedy': "Comedy",
        'adventure': "Adventure",
        'drama': "Drama"
    }

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=BOOK_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    page = models.PositiveIntegerField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', null=True)
