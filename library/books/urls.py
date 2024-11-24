from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='Book_list'),
    path('create_book/', views.create_book, name='Create_book'),
    path('update_book/<int:id>/', views.update_book, name='Update_book'),
    path('delete_book/<int:id>/', views.delete_book, name='Delete_book'),
    path('detail_book/<int:id>/', views.detail_book, name='Detail_book'),
]
