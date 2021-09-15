from django.db import models
from django.contrib.auth.models import User

class Customer(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    address = models.Charfield(max_length=100, blank=True, null=True)
    zip_code = models.IntegerField(max_length=5, min_length=5, null=True)

