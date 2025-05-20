from django.db import models
from EventoSismico.models import EventoSismico
from sismologia.models import Sismografo

# Create your models here.
class SerieTemporal(models.Model):
    _condicion_alarma = models.IntegerField(db_column='condicion_alarma')
    _fecha_hora_registro_muestras = models.DateTimeField(db_column='fecha_hora_registro_muestras')
    _fecha_hora_registro = models.DateTimeField(db_column='fecha_hora_registro')
    _frecuencia_muestreo = models.FloatField(db_column='frecuencia_muestreo')

    _evento_sismico = models.ForeignKey('EventoSismico.EventoSismico', on_delete=models.CASCADE, related_name="series_temporales", db_column='evento_sismico')
    _sismografo = models.ForeignKey('sismologia.Sismografo', on_delete=models.CASCADE, related_name="series_temporales", db_column='sismografo')

    @property
    def evento_sismico(self):
        return self._evento_sismico

    @evento_sismico.setter
    def evento_sismico(self, value):
        self._evento_sismico = value

    @property
    def sismografo(self):
        return self._sismografo

    @sismografo.setter
    def sismografo(self, value):
        self._sismografo = value

    @property
    def condicion_alarma(self):
        return self._condicion_alarma

    @condicion_alarma.setter
    def condicion_alarma(self, value):
        self._condicion_alarma = value

    @property
    def fecha_hora_registro_muestras(self):
        return self._fecha_hora_registro_muestras

    @fecha_hora_registro_muestras.setter
    def fecha_hora_registro_muestras(self, value):
        self._fecha_hora_registro_muestras = value

    @property
    def fecha_hora_registro(self):
        return self._fecha_hora_registro

    @fecha_hora_registro.setter
    def fecha_hora_registro(self, value):
        self._fecha_hora_registro = value

    @property
    def frecuencia_muestreo(self):
        return self._frecuencia_muestreo

    @frecuencia_muestreo.setter
    def frecuencia_muestreo(self, value):
        self._frecuencia_muestreo = value


class MuestraSismica(models.Model):
    _fecha_hora_muestra = models.DateTimeField(db_column='fecha_hora_muestra')
    _serie_temporal = models.ForeignKey(SerieTemporal, on_delete=models.CASCADE, related_name="muestras", db_column='serie_temporal')

    @property
    def fecha_hora_muestra(self):
        return self._fecha_hora_muestra

    @fecha_hora_muestra.setter
    def fecha_hora_muestra(self, value):
        self._fecha_hora_muestra = value

    @property
    def serie_temporal(self):
        return self._serie_temporal

    @serie_temporal.setter
    def serie_temporal(self, value):
        self._serie_temporal = value


class DetalleMuestraSismica(models.Model):
    _valor = models.FloatField(db_column='valor')
    _muestra = models.ForeignKey(MuestraSismica, on_delete=models.CASCADE, related_name="detalles", db_column='muestra')

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = value

    @property
    def muestra(self):
        return self._muestra

    @muestra.setter
    def muestra(self, value):
        self._muestra = value
