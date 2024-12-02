from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book


def index(request):
    books = Book.objects.all()
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'index.html', context={'books': books, 'form': form})

