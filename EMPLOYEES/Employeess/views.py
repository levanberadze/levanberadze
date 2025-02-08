from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializer import EmployeeSerializer


class CreateView(generics.CreateAPIView):
    quaryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer