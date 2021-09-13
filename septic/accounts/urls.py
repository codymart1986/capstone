from django.urls import path
from django.urls import path
from . import views

app_name = "accounts"
urlspatterns = [
    path('register/', views.RegisterView.as_view(), name='register')
]