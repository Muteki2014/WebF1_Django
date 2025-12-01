from rest_framework import generics
from circuitos.models import Circuito
from .serializers import CircuitoSerializer

class CircuitoListAPI(generics.ListCreateAPIView):
    queryset = Circuito.objects.all()
    serializer_class = CircuitoSerializer

class CircuitoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Circuito.objects.all()
    serializer_class = CircuitoSerializer   