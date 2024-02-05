from rest_framework import serializers
from .models import Jersey

class JerseySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jersey
        fields = '__all__'
