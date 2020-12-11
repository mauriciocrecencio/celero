from rest_framework import serializers

class GameSerializer(serializers.Serializer):
    name = serializers.CharField()
    year = serializers.IntegerField()
    season = serializers.CharField() 
    city = serializers.CharField()

class SportSerializer(serializers.Serializer):
    name = serializers.CharField()
    game = serializers.SerializerMethodField('get_game')

    def get_game(self, sport):
        game = sport.game_id
        return GameSerializer(game).data