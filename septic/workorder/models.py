from django.db import models

class Workorder(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True)
    hours=models.IntegerField(default=1, null=True, blank=True)
    description=models.CharField(max_length=255, null=True, blank=True)
    body=models.CharField(max_length=255, null=True, blank=True)
    recommendations=models.CharField(max_length=255, null=True, blank=True)