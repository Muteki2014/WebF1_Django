from rest_framework import serializers
from pilotos.models import Piloto

class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'
