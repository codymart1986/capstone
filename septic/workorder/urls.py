from django.urls import path, include
from . import views


app_name = "workorder"
urlpatterns = [
    path('workorder/', views.create, name='create'),
]