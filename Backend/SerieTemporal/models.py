from django.db import models
from EventoSismico.models import EventoSismico
from sismologia.models import Sismografo

# Create your models here.
class SerieTemporal(models.Model):
    evento_sismico = models.ForeignKey(EventoSismico, on_delete=models.CASCADE, related_name='series_temporales')
    sismografo = models.ForeignKey(Sismografo, on_delete=models.SET_NULL, null=True)
    fecha_hora_inicio_registro_muestras = models.DateTimeField()
    frecuencia_muestreo = models.FloatField()
    condicion_alarma = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Serie de {self.evento_sismico} desde {self.fecha_hora_inicio_registro_muestras}"

class MuestraSismica(models.Model):
    serie_temporal = models.ForeignKey(SerieTemporal, on_delete=models.CASCADE, related_name='muestras')
    fecha_hora_muestra = models.DateTimeField()

    def __str__(self):
        return f"Muestra de {self.fecha_hora_muestra}"

class TipoDato(models.Model):
    denominacion = models.CharField(max_length=100)
    nombre_unidad_medida = models.CharField(max_length=50)
    valor_umbral = models.FloatField()

    def __str__(self):
        return self.denominacion
    
class DetalleMuestraSismica(models.Model):
    muestra = models.ForeignKey(MuestraSismica, on_delete=models.CASCADE, related_name='detalles')
    tipo_dato = models.ForeignKey(TipoDato, on_delete=models.CASCADE)
    valor = models.FloatField()

    def __str__(self):
        return f"{self.tipo_dato}: {self.valor}"
