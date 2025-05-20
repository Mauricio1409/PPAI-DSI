from django.db import models
from estados.models import Estado
# Create your models here.


class MagnitudRichter(models.Model):
    numero = models.IntegerField()
    descripcion_magnitud = models.TextField()

class AlcanceSismo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class ClasificacionSismo(models.Model):
    nombre = models.CharField(max_length=100)
    km_profundidad_desde = models.FloatField()
    km_profundidad_hasta = models.FloatField()

class OrigenDeGeneracion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class EventoSismico(models.Model):
    fecha_hora_ocurrencia = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField(null=True, blank=True)
    latitud_epicentro = models.FloatField()
    longitud_epicentro = models.FloatField()
    latitud_hipocentro = models.FloatField()
    longitud_hipocentro = models.FloatField()
    valor_magnitud = models.FloatField()

    magnitud = models.ForeignKey(MagnitudRichter, on_delete=models.CASCADE)
    alcance = models.ForeignKey(AlcanceSismo, on_delete=models.CASCADE)
    clasificacion = models.ForeignKey(ClasificacionSismo, on_delete=models.CASCADE)
    origen = models.ForeignKey(OrigenDeGeneracion, on_delete=models.CASCADE)
    
    estado_actual = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, related_name="estado_actual_eventos")