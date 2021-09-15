from django.db import models
from django.contrib.auth.models import User

class Employee(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
