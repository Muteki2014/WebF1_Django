from rest_framework import serializers
from circuitos.models import Circuito

class CircuitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuito
        fields = '__all__'
