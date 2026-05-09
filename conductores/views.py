from rest_framework import generics
from .models import Conductor
from .serializers import ConductorSerializer

class ConductorListCreateView(generics.ListCreateAPIView):

    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer


class ConductorDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer