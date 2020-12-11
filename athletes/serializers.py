from rest_framework import serializers
from .models import Athlete, Athlete_instance
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

class AthleteInstanceSerializer(serializers.ModelSerializer):
    event_id = EventSerializer()
    class Meta:
        model = Athlete_instance
        fields = ('age', 'medal', 'event_id')
    # age = serializers.CharField()
    # medal = serializers.CharField()
    # event_id = 
    # athlete_id
    # height
    # weight