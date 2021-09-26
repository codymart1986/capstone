from django.urls import path

from . import views


app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('edit/<int:option>/', views.edit, name="edit")
]