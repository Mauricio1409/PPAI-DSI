from django.db import models
from estados.models import Estado

# Create your models here.
class EstacionSismologica(models.Model):
    codigo_estacion = models.CharField(max_length=100)
    documento_certificacion_adq = models.CharField(max_length=100)
    fecha_solicitud_certificacion = models.DateTimeField()
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    numero_certificacion_adquisicion = models.CharField(max_length=100)

class Sismografo(models.Model):
    identificador_sismografo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    fecha_adquisicion = models.DateTimeField()
    estacion = models.ForeignKey(EstacionSismologica, on_delete=models.CASCADE)

    estado_actual = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, related_name="estado_actual_sismografos")