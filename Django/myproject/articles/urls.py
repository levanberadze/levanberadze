from django.urls import path
from .import views

urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('create_article/', views.create_article, name='create-article')
]