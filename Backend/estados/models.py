from django.db import models
from EventoSismico.models import EventoSismico
from sismologia.models import Sismografo
from usuarios.models import Empleado
# Create your models here.

class Estado(models.Model):
    AMBITO_CHOICES = [
        ('evento', 'Evento Sísmico'),
        ('sismografo', 'Sismógrafo'),
    ]

    nombre = models.CharField(max_length=100)
    ambito = models.CharField(max_length=15, choices=AMBITO_CHOICES)

class CambioEstado(models.Model):
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField(null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    evento_sismico = models.ForeignKey(EventoSismico, on_delete=models.CASCADE, null=True, blank=True, related_name="cambios_estado")
    sismografo = models.ForeignKey(Sismografo, on_delete=models.CASCADE, null=True, blank=True, related_name="cambios_estado")
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)