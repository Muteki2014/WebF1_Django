from rest_framework import generics
from pilotos.models import Piloto
from .serializers import PilotoSerializer

class PilotoListAPI(generics.ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer

class PilotoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
