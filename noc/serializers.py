from rest_framework import serializers

class NocSerializer(serializers.Serializer):
    name = serializers.CharField()
    region = serializers.CharField()
    notes = serializers.CharField()