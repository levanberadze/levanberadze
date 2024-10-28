from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_article/', views.create_article, name='create_article'),
    path('articles/', views.view_articles, name='view_articles'),
    path('articles/<int:pk>', views.view_article, name='view_article')
]