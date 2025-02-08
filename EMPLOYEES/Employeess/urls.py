from django.urls import path
from .views import CreateView, EmployeeView

urlpatterns = [
    path('employees/', CreateView.as_view(), name='employee create'),
    path('employees/<int:pk>/', EmployeeView.as_view(), name='employee'),
]
