from django.db import models

# Create your models here.

class Athlete(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    noc = models.CharField(max_length=100)
    games = models.CharField(max_length=255)
    year = models.IntegerField()
    season = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    event = models.CharField(max_length=255)
    medal = models.CharField(max_length=100)
