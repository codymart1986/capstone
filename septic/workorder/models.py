from django.db import models

class Workorder(models.model):
    name=models.CharField(max_length=50, null=True, blank=True)
    description=models.CharField(max_length=255, null=True, blank=True)
    hours=models.IntegerField(default=1, null=True)
    body=models.CharField(max_length=255, null=True, blank=True)