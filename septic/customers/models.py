from django.db import models
from django.db.models.fields import EmailField

class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.user', blank=True, null=True, on_delete=models.PROTECT)
    address = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.IntegerField(default=00000, null=True)
    balance = models.IntegerField(default=0)
    email = EmailField(max_length=100)