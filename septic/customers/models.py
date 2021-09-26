from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.PROTECT)
    zip_code = models.IntegerField(default=00000, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    emergency_form = models.CharField(max_length=255, blank=True, null=True)
