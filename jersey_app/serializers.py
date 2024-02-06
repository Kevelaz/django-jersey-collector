from rest_framework import serializers
from .models import Jersey, Team,Club

class JerseySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jersey
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('jersey',)

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'