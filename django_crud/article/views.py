from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

def create_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('create_article')
    return render(request, 'create_article.html', context={'form': form})

def view_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', context={'articles': articles})

def view_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article.html', context={'article': article})

