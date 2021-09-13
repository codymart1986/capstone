from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import CustomUserForm

class RegisterView(generic.CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'