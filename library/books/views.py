from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.filter(rating__gt=6)
    return render(request, 'books/book_list.html', context={'books': books})


def detail_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail_book')
        return render(request, 'detail_book.html', context={'book': book})


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, 'update_book.html', context={'form': form})


def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, 'update_book.html', context={'form': form})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')