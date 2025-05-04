from django.db import models

# Create your models here.
class EstacionSismologica(models.Model):
    nombre = models.CharField(max_length=100)
    documento_certificacion_adq = models.FileField(upload_to='certificaciones/', null=True, blank=True)
    fecha_solicitud_certificacion = models.DateField()
    nro_certificacion_adquisicion = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return f"{self.nombre} ({self.codigo_estacion})"

class Sismografo(models.Model):
    nro_serie = models.CharField(max_length=100)
    fecha_adquisicion = models.DateField()

    estacion = models.ForeignKey(EstacionSismologica, on_delete=models.CASCADE, related_name='sismografos')

    def __str__(self):
        return f"{self.identificador_sismografo} (Serie {self.nro_serie})"
