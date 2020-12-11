from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    season = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    
class Sport(models.Model):
    name = models.CharField(max_length=255)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
