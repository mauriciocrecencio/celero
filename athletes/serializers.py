from rest_framework import serializers
from .models import Athlete

class AthleteSerializer(serializers.Serializer):
    name = serializers.CharField()
    