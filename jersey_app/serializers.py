from rest_framework import serializers
from .models import Jersey, Team,Club


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class JerseySerializer(serializers.ModelSerializer):
    clubs = ClubSerializer(many=True, read_only=True)
    
    class Meta:
        model = Jersey
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('jersey',)

