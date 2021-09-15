from django.urls import path
from .views import EmployeeList

urlpatterns = [
    path('', views.EmployeeList.as_view())
]