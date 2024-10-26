from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/templates/article_list.html')

def create_article(request):
    if request.method == "POST":
        articleform = ArticleForm(request.POST)
        if articleform.is_valid():
            articleform.save()
            return redirect('article_list')
        else:
            articleform = ArticleForm()
        return render(request, 'articles/create_article.html')
