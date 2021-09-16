from django.db import models

class Employee(models.Model):
    user = models.ForeignKey('accounts.User', blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, default="")

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name