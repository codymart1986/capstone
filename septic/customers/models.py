from django.db import models


class Customer(models.Model):
    user = models.ForeignKey('accounts.User', blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.IntegerField(max_length=5, null=True)

