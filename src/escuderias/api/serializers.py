from rest_framework import serializers
from escuderias.models import Escuderia

class EscuderiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuderia
        fields = '__all__'
