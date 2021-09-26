from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=50, default="")
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.PROTECT)
    zip_code = models.IntegerField(default=00000, null=True)