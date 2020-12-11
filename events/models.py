from django.db import models
from sports.models import Sport
# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=255)
    sport_id = models.ForeignKey(Sport, on_delete=models.CASCADE)