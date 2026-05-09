from django.db import models
from conductores.models import Conductor

class Ruta(models.Model):

    origen = models.CharField(max_length=100)

    destino = models.CharField(max_length=100)

    horario = models.CharField(max_length=50)

    conductor = models.ForeignKey(
        Conductor,
        on_delete=models.CASCADE,
        related_name='rutas'
    )

    def __str__(self):
        return f"{self.origen} - {self.destino}"

