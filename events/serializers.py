from rest_framework import serializers
from sports.serializers import SportSerializer

class EventSerializer(serializers.Serializer):
    name = serializers.CharField()
    sport = serializers.SerializerMethodField('get_sport')
    
    def get_sport(self,event):
        sport = event.sport_id
        return SportSerializer(sport).data