from django.db import models
from estados.models import Estado

# Create your models here.
class EstacionSismologica(models.Model):
    _codigo_estacion = models.CharField(max_length=100)
    _documento_certificacion_adq = models.CharField(max_length=100)
    _fecha_solicitud_certificacion = models.DateTimeField()
    _nombre = models.CharField(max_length=100)
    _latitud = models.FloatField()
    _longitud = models.FloatField()
    _numero_certificacion_adquisicion = models.CharField(max_length=100)

    @property
    def codigo_estacion(self):
        return self._codigo_estacion

    @codigo_estacion.setter
    def codigo_estacion(self, value):
        self._codigo_estacion = value

    @property
    def documento_certificacion_adq(self):
        return self._documento_certificacion_adq

    @documento_certificacion_adq.setter
    def documento_certificacion_adq(self, value):
        self._documento_certificacion_adq = value

    @property
    def fecha_solicitud_certificacion(self):
        return self._fecha_solicitud_certificacion

    @fecha_solicitud_certificacion.setter
    def fecha_solicitud_certificacion(self, value):
        self._fecha_solicitud_certificacion = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def latitud(self):
        return self._latitud

    @latitud.setter
    def latitud(self, value):
        self._latitud = value

    @property
    def longitud(self):
        return self._longitud

    @longitud.setter
    def longitud(self, value):
        self._longitud = value

    @property
    def numero_certificacion_adquisicion(self):
        return self._numero_certificacion_adquisicion

    @numero_certificacion_adquisicion.setter
    def numero_certificacion_adquisicion(self, value):
        self._numero_certificacion_adquisicion = value


class Sismografo(models.Model):
    _identificador_sismografo = models.CharField(max_length=100)
    _numero_serie = models.CharField(max_length=100)
    _fecha_adquisicion = models.DateTimeField()
    _estacion = models.ForeignKey(EstacionSismologica, on_delete=models.CASCADE)
    _estado_actual = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, related_name="estado_actual_sismografos")

    @property
    def identificador_sismografo(self):
        return self._identificador_sismografo

    @identificador_sismografo.setter
    def identificador_sismografo(self, value):
        self._identificador_sismografo = value

    @property
    def numero_serie(self):
        return self._numero_serie

    @numero_serie.setter
    def numero_serie(self, value):
        self._numero_serie = value

    @property
    def fecha_adquisicion(self):
        return self._fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, value):
        self._fecha_adquisicion = value

    @property
    def estacion(self):
        return self._estacion

    @estacion.setter
    def estacion(self, value):
        self._estacion = value

    @property
    def estado_actual(self):
        return self._estado_actual

    @estado_actual.setter
    def estado_actual(self, value):
        self._estado_actual = value