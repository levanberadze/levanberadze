from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('create', views.teacher_create, name='teacher_create'),
    path('update/<int:id>', views.teacher_update, name='teacher_update'),
    path('delete/<int:id>', views.teacher_delete, name='teacher_delete')
]