from django.db import models

# Create your models here.


class ClasificacionSismo(models.Model):
    nombre = models.CharField(max_length=100)
    km_profundidad_desde = models.FloatField()
    km_profundidad_hasta = models.FloatField()

    def __str__(self):
        return self.nombre

class MagnitudRichter(models.Model):
    descripcion_magnitud = models.CharField(max_length=100)
    numero = models.FloatField()

    def __str__(self):
        return f"{self.descripcion_magnitud} ({self.numero})"

class OrigenDeGeneracion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class AlcanceSismo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre_estado = models.CharField(max_length=100)
    ambito = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_estado


class EventoSismico(models.Model):
    fecha_hora_ocurrencia = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField(null=True, blank=True)
    latitud_epicentro = models.FloatField()
    longitud_epicentro = models.FloatField()
    latitud_hipocentro = models.FloatField()
    longitud_hipocentro = models.FloatField()
    valor_magnitud = models.FloatField()

    clasificacion = models.ForeignKey(ClasificacionSismo, on_delete=models.SET_NULL, null=True)
    magnitud = models.ForeignKey(MagnitudRichter, on_delete=models.SET_NULL, null=True)
    origen = models.ForeignKey(OrigenDeGeneracion, on_delete=models.SET_NULL, null=True)
    alcance = models.ForeignKey(AlcanceSismo, on_delete=models.SET_NULL, null=True)

    def estado_actual(self):
        return self.cambios_estado.filter(fecha_hora_fin__isnull=True).first()
    
class CambioEstado(models.Model):
    evento = models.ForeignKey(EventoSismico, on_delete=models.CASCADE, related_name='cambios_estado')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField(null=True, blank=True)

    def es_estado_actual(self):
        return self.fecha_hora_fin is None
    