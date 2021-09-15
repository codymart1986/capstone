from django.urls import path
from .views import CustomerList

urlpatterns = [
    path('', views.CustomerList.as_view())
]