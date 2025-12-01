from rest_framework import generics
from escuderias.models import Escuderia
from .serializers import EscuderiaSerializer

class EscuderiaListAPI(generics.ListCreateAPIView):
    queryset = Escuderia.objects.all()
    serializer_class = EscuderiaSerializer
class EscuderiaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Escuderia.objects.all()
    serializer_class = EscuderiaSerializer   