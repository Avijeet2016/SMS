from django.urls import path
from .views import create_employee

urlpatterns = [
    path('employee/create', create_employee, name="create-employee"),
    
]