from django.db import models
from EventoSismico.models import EventoSismico
from sismologia.models import Sismografo

# Create your models here.
class SerieTemporal(models.Model):
    condicion_alarma = models.IntegerField()
    fecha_hora_registro_muestras = models.DateTimeField()
    fecha_hora_registro = models.DateTimeField()
    frecuencia_muestreo = models.FloatField()

    evento_sismico = models.ForeignKey(EventoSismico, on_delete=models.CASCADE, related_name="series_temporales")
    sismografo = models.ForeignKey(Sismografo, on_delete=models.CASCADE, related_name="series_temporales")

class MuestraSismica(models.Model):
    fecha_hora_muestra = models.DateTimeField()
    serie_temporal = models.ForeignKey(SerieTemporal, on_delete=models.CASCADE, related_name="muestras")

class DetalleMuestraSismica(models.Model):
    valor = models.FloatField()
    muestra = models.ForeignKey(MuestraSismica, on_delete=models.CASCADE, related_name="detalles")
