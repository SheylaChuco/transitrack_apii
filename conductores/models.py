from django.db import models

class Conductor(models.Model):

    nombre = models.CharField(max_length=100)

    numero_licencia = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.nombre
# Create your models here.
