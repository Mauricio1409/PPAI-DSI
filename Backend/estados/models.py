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

    _nombre = models.CharField(max_length=100, db_column='nombre')
    _ambito = models.CharField(max_length=15, choices=AMBITO_CHOICES, db_column='ambito')

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def ambito(self):
        return self._ambito

    @ambito.setter
    def ambito(self, value):
        self._ambito = value


class CambioEstado(models.Model):
    _fecha_hora_inicio = models.DateTimeField(db_column='fecha_hora_inicio')
    _fecha_hora_fin = models.DateTimeField(null=True, blank=True, db_column='fecha_hora_fin')
    _estado = models.ForeignKey(Estado, on_delete=models.CASCADE, db_column='estado_id')

    _evento_sismico = models.ForeignKey(
        EventoSismico, on_delete=models.CASCADE, null=True, blank=True,
        related_name="cambios_estado", db_column='evento_sismico_id'
    )
    _sismografo = models.ForeignKey(
        Sismografo, on_delete=models.CASCADE, null=True, blank=True,
        related_name="cambios_estado", db_column='sismografo_id'
    )
    _empleado = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, null=True, blank=True,
        db_column='empleado_id'
    )

    @property
    def fecha_hora_inicio(self):
        return self._fecha_hora_inicio

    @fecha_hora_inicio.setter
    def fecha_hora_inicio(self, value):
        self._fecha_hora_inicio = value

    @property
    def fecha_hora_fin(self):
        return self._fecha_hora_fin

    @fecha_hora_fin.setter
    def fecha_hora_fin(self, value):
        self._fecha_hora_fin = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

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
    def empleado(self):
        return self._empleado

    @empleado.setter
    def empleado(self, value):
        self._empleado = value