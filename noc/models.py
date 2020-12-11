from django.db import models

# Create your models here.
class Noc(models.Model):
    name = models.CharField(max_length=4)
    region = models.CharField(max_length=100)
    notes = models.CharField(max_length=255, blank=True, null=True)