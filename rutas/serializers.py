from rest_framework import serializers
from .models import Ruta

class RutaSerializer(serializers.ModelSerializer):

    conductor_nombre = serializers.CharField(
        source='conductor.nombre',
        read_only=True
    )

    class Meta:
        model = Ruta
        fields = '__all__'