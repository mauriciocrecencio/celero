from django.db import models
from noc.models import Noc
from events.models import Event
class Athlete(models.Model):
    GENDER_TYPES = [('M', 'M'),('F', 'F')]
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDER_TYPES)
    team = models.CharField(max_length=100)
    noc = models.ForeignKey(Noc, on_delete=models.CASCADE)

class AthleteInstance(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    event = models.ManyToManyField(Event)
    medal = models.CharField(max_length=20)
    age = models.IntegerField()
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
