from books_2.models import Book, Author
from django.db.models import Sum, Avg


def run():
    # Book.objects.all().update(author=Author.objects.first())

    total_price = Book.objects.aggregate(Sum('price'))
    avg = Book.objects.aggregate(Avg('price'))
    print(total_price)
    print(avg)