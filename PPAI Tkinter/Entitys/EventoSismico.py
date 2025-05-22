from Entitys.Estado import Estado
from Entitys.CambioEstado import CambioEstado
from Entitys.ClasificacionSismo import ClasificacionSismo
from Entitys.OrigenDeGeneracion import OrigenDeGeneracion
from Entitys.AlcanceSismo import AlcanceSismo
from Entitys.SerieTemporal import SerieTemporal
from datetime import datetime

class EventoSismico:
    def __init__(self, fechaHoraOcurrencia: datetime, magnitud: float, latitud: float, longitud: float, cambioEstado : list[CambioEstado], estado : Estado, clasificacionSismo : ClasificacionSismo, alcanceSismo : AlcanceSismo, origenGenercion : OrigenDeGeneracion, serieTemporal : list[SerieTemporal]):
        self._cambioEstadoActual = None
        self._fechaHoraFin = None
        self._fechaHoraOcurrencia = fechaHoraOcurrencia
        self._latitudEpicentro = latitud
        self._latitudHipocentro = latitud
        self._longitudEpicentro = longitud
        self._longitudHipocentro = longitud
        self._ValorMagnitud = magnitud
        self._cambioEstado = cambioEstado
        self._estado = estado
        self._alcanceSismo = alcanceSismo
        self._origenGeneracion = origenGenercion
        self._clasificacionSismo = clasificacionSismo
        self._seriesTemporales = serieTemporal

    #region Getters y Setters
    @property
    def ValorMagnitud(self):
        return self._ValorMagnitud
    @ValorMagnitud.setter
    def ValorMagnitud(self, valor: float):
        self._ValorMagnitud = valor

    @property
    def fechaHoraOcurrencia(self):
        return self._fechaHoraOcurrencia
    @fechaHoraOcurrencia.setter
    def fechaHoraOcurrencia(self, value: datetime):
        self._fechaHoraOcurrencia = value

    @property
    def fechaHoraFin(self):
        return self._fechaHoraFin
    @fechaHoraFin.setter
    def fechaHoraFin(self, value: datetime):
        self._fechaHoraFin = value

    @property
    def latitudHipocentro(self):
        return self._latitudHipocentro
    @latitudHipocentro.setter
    def latitudHipocentro(self, value: float):
        self._latitudHipocentro = value

    @property
    def longitudHipocentro(self):
        return self._longitudHipocentro
    @longitudHipocentro.setter
    def longitudHipocentro(self, value: float):
        self._longitudHipocentro = value

    @property
    def latitudEpicentro(self):
        return self._latitudEpicentro
    @latitudEpicentro.setter
    def latitudEpicentro(self, value: float):
        self._latitudEpicentro = value

    @property
    def longitudEpicentro(self):
        return self._longitudEpicentro
    @longitudEpicentro.setter
    def longitudEpicentro(self, value: float):
        self._longitudEpicentro = value

    @property
    def alcanceSismo(self):
        return self._alcanceSismo

    @alcanceSismo.setter
    def alcanceSismo(self, nuevoAlcanceSismo : AlcanceSismo):
        self._alcanceSismo = nuevoAlcanceSismo

    @property
    def origenGeneracion(self):
        return self._origenGeneracion

    @origenGeneracion.setter
    def origenGeneracion(self, nuevoOrigenGeneracion : origenGeneracion):
        self._origenGeneracion = nuevoOrigenGeneracion

    @property
    def clasificacionSismo(self):
        return self._clasificacionSismo

    @clasificacionSismo.setter
    def clasificacionSismo(self, nuevoClasificacionSismo : clasificacionSismo):
        self._clasificacionSismo = nuevoClasificacionSismo

    @property
    def seriesTemporales(self):
        return self._seriesTemporales
    #endregion

    def esPendienteRevision(self):
        return self._estado.sosPendienteRevision()
    
    def getUbicacion(self):
        return ((self._latitudEpicentro, self._longitudEpicentro),(self._latitudHipocentro, self._longitudHipocentro)) # TODO CHEQUEAR ESTO CON EL DIAGRAMA

    def revisar(self, estado, Analista , fechaHoraActual):
        self._estado = estado
        self.buscarCambioEstadoActual()
        self._cambioEstadoActual.setFechaHoraFin(fechaHoraActual)
        self.cambiarCambioEstado(estado, Analista, fechaHoraActual)

    def cambiarCambioEstado(self, estado, analista, fechaHoraActual):
        nuevoCambioEstado = CambioEstado(fechaHoraActual, estado, analista)
        self._cambioEstado.append(nuevoCambioEstado)
        self._cambioEstadoActual = nuevoCambioEstado


    #TODO MODIFICAR ESTO EN EL DIAGRAMA DE SECUENCIA (nombre método)
    def buscarCambioEstadoActual(self):
        for cambio in self._cambioEstado:
            if cambio.sosActual():
                self._cambioEstadoActual = cambio
        return None


    def obtenerDatos(self):
        alcance = self._alcanceSismo.getNombre()
        clasificacion = self._clasificacionSismo.getNombre()
        origen =self._origenGeneracion.obtenerOrigen()

        return {
            f"alcanceSismo": alcance,
            f"clasificacionSismo": clasificacion,
            f"origenGeneracion": origen,
            f"seriesTemporales": [serie.obtenerDatos() for serie in self._seriesTemporales]
        }

