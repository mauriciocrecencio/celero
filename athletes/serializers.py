from rest_framework import serializers
from .models import Athlete
from noc.serializers import NocSerializer
from events.serializers import EventSerializer
class AthleteSerializer(serializers.Serializer):
    name = serializers.CharField()
    gender = serializers.CharField()
    team = serializers.CharField()
    noc = serializers.SerializerMethodField('get_noc')

    def get_noc(self, athlete):
        noc = athlete.noc
        return NocSerializer(noc).data

class AthleteInstanceSerializer(serializers.Serializer):
    age = serializers.CharField()
    medal = serializers.CharField()
    height = serializers.CharField()
    weight = serializers.CharField()
    event_id = serializers.SerializerMethodField('get_event')
    athlete_id = serializers.SerializerMethodField('get_athlete')

    def get_event(self, athlete_instance):
        event = athlete_instance.event
        return EventSerializer(event, many=True).data

    def get_athlete(self, athlete_instance):
        athlete = athlete_instance.athlete
        return AthleteSerializer(athlete).data