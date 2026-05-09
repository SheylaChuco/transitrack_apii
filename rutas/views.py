
from rest_framework import generics, filters
from .models import Ruta
from .serializers import RutaSerializer

class RutaListCreateView(generics.ListCreateAPIView):

    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = ['origen', 'destino']


class RutaDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
# Create your views here.
