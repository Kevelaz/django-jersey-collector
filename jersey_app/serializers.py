from rest_framework import serializers
from .models import Jersey, Team

class JerseySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jersey
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('jersey',)