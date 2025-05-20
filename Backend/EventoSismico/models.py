from django.db import models
from estados.models import Estado


class MagnitudRichter(models.Model):
    _numero = models.IntegerField()
    _descripcion_magnitud = models.TextField()

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def descripcion_magnitud(self):
        return self._descripcion_magnitud

    @descripcion_magnitud.setter
    def descripcion_magnitud(self, value):
        self._descripcion_magnitud = value


class AlcanceSismo(models.Model):
    _nombre = models.CharField(max_length=100)
    _descripcion = models.TextField()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value


class ClasificacionSismo(models.Model):
    _nombre = models.CharField(max_length=100)
    _km_profundidad_desde = models.FloatField()
    _km_profundidad_hasta = models.FloatField()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def km_profundidad_desde(self):
        return self._km_profundidad_desde

    @km_profundidad_desde.setter
    def km_profundidad_desde(self, value):
        self._km_profundidad_desde = value

    @property
    def km_profundidad_hasta(self):
        return self._km_profundidad_hasta

    @km_profundidad_hasta.setter
    def km_profundidad_hasta(self, value):
        self._km_profundidad_hasta = value


class OrigenDeGeneracion(models.Model):
    _nombre = models.CharField(max_length=100)
    _descripcion = models.TextField()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

# --------------------------------------------
# EVENTO SÍSMICO
# --------------------------------------------

class EventoSismico(models.Model):
    _fecha_hora_ocurrencia = models.DateTimeField()
    _fecha_hora_fin = models.DateTimeField(null=True, blank=True)
    _latitud_epicentro = models.FloatField()
    _longitud_epicentro = models.FloatField()
    _latitud_hipocentro = models.FloatField()
    _longitud_hipocentro = models.FloatField()
    _valor_magnitud = models.FloatField()

    _magnitud = models.ForeignKey(MagnitudRichter, on_delete=models.CASCADE)
    _alcance = models.ForeignKey(AlcanceSismo, on_delete=models.CASCADE)
    _clasificacion = models.ForeignKey(ClasificacionSismo, on_delete=models.CASCADE)
    _origen = models.ForeignKey(OrigenDeGeneracion, on_delete=models.CASCADE)

    _estado_actual = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, related_name="estado_actual_eventos")

    # Getters y setters
    @property
    def fecha_hora_ocurrencia(self):
        return self._fecha_hora_ocurrencia

    @fecha_hora_ocurrencia.setter
    def fecha_hora_ocurrencia(self, value):
        self._fecha_hora_ocurrencia = value

    @property
    def fecha_hora_fin(self):
        return self._fecha_hora_fin

    @fecha_hora_fin.setter
    def fecha_hora_fin(self, value):
        self._fecha_hora_fin = value

    @property
    def latitud_epicentro(self):
        return self._latitud_epicentro

    @latitud_epicentro.setter
    def latitud_epicentro(self, value):
        self._latitud_epicentro = value

    @property
    def longitud_epicentro(self):
        return self._longitud_epicentro

    @longitud_epicentro.setter
    def longitud_epicentro(self, value):
        self._longitud_epicentro = value

    @property
    def latitud_hipocentro(self):
        return self._latitud_hipocentro

    @latitud_hipocentro.setter
    def latitud_hipocentro(self, value):
        self._latitud_hipocentro = value

    @property
    def longitud_hipocentro(self):
        return self._longitud_hipocentro

    @longitud_hipocentro.setter
    def longitud_hipocentro(self, value):
        self._longitud_hipocentro = value

    @property
    def valor_magnitud(self):
        return self._valor_magnitud

    @valor_magnitud.setter
    def valor_magnitud(self, value):
        self._valor_magnitud = value

    @property
    def magnitud(self):
        return self._magnitud

    @magnitud.setter
    def magnitud(self, value):
        self._magnitud = value

    @property
    def alcance(self):
        return self._alcance

    @alcance.setter
    def alcance(self, value):
        self._alcance = value

    @property
    def clasificacion(self):
        return self._clasificacion

    @clasificacion.setter
    def clasificacion(self, value):
        self._clasificacion = value

    @property
    def origen(self):
        return self._origen

    @origen.setter
    def origen(self, value):
        self._origen = value

    @property
    def estado_actual(self):
        return self._estado_actual

    @estado_actual.setter
    def estado_actual(self, value):
        self._estado_actual = value
        
    def actualizar_estado_rechazado(self, empleado, fecha_hora, estado):
        self.estado_actual = estado
        self.save()
        self.cambios_estado.create(
            empleado=empleado,
            fecha_hora_inicio=fecha_hora,
            estado=estado,
            evento_sismico=self,
            sismografo=None, 
        )
