from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('create_post/', views.create_post, name='create_post'),
    path('post<int:pk>', views.Post, name='post')
]