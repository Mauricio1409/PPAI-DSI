from Entitys.AnalistaSismos import AnalistaSismos
from Entitys.MagnitudRichter import MagnitudRichter
from Entitys.STATE.AutoDetectado import AutoDetectado
from Entitys.STATE.Estado import Estado
from Entitys.CambioEstado import CambioEstado
from Entitys.ClasificacionSismo import ClasificacionSismo
from Entitys.OrigenDeGeneracion import OrigenDeGeneracion
from Entitys.AlcanceSismo import AlcanceSismo
from Entitys.SerieTemporal import SerieTemporal
from datetime import datetime

class EventoSismico:
    def __init__(self, fechaHoraOcurrencia: datetime, magnitud: MagnitudRichter, latitud_hipocentro: float,
                 longitud_hipocentro: float, cambioEstado : list[CambioEstado], estado : Estado,
                 clasificacionSismo : ClasificacionSismo, latitud_epicentro : float, longitud_epicentro : float,
                 alcanceSismo : AlcanceSismo, origenGenercion : OrigenDeGeneracion, seriesTemporales : list[SerieTemporal],
                 valorMagnitud: float, eventoSismicoId: int = None):

        self._cambioEstadoActual: CambioEstado|None = None
        self._fechaHoraFin: datetime|None = None
        self._eventoSismicoId: int = eventoSismicoId
        self._fechaHoraOcurrencia: datetime = fechaHoraOcurrencia
        self._latitudEpicentro: float = latitud_epicentro
        self._latitudHipocentro: float = latitud_hipocentro
        self._longitudEpicentro: float = longitud_epicentro
        self._longitudHipocentro: float = longitud_hipocentro
        self._magnitudRitcher: MagnitudRichter = magnitud
        self.valorMagnitud: float = valorMagnitud
        self._cambioEstado: list[CambioEstado] = cambioEstado
        self._estado: Estado = estado
        self._alcanceSismo: AlcanceSismo = alcanceSismo
        self._origenGeneracion: OrigenDeGeneracion = origenGenercion
        self._clasificacionSismo: ClasificacionSismo = clasificacionSismo
        self._seriesTemporales: list[SerieTemporal] = seriesTemporales

    #region Getters y Setters
    @property
    def magnitud(self):
        return self._magnitudRitcher
    @property
    def valorMagnitud(self):
        return self._ValorMagnitud
    @valorMagnitud.setter
    def valorMagnitud(self, valor: float):
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
    def origenGeneracion(self, nuevoOrigenGeneracion : OrigenDeGeneracion):
        self._origenGeneracion = nuevoOrigenGeneracion

    @property
    def clasificacionSismo(self):
        return self._clasificacionSismo

    @clasificacionSismo.setter
    def clasificacionSismo(self, nuevoClasificacionSismo : ClasificacionSismo):
        self._clasificacionSismo = nuevoClasificacionSismo

    @property
    def seriesTemporales(self):
        return self._seriesTemporales
    
    @property
    def cambioEstado(self):
        return self._cambioEstado
    
    @cambioEstado.setter
    def cambioEstado(self, nuevoCambioEstado : list[CambioEstado]):
        self._cambioEstado = nuevoCambioEstado

    @property
    def cambioEstadoActual(self):
        return self._cambioEstadoActual
    @cambioEstadoActual.setter
    def cambioEstadoActual(self, nuevoCambioEstadoActual : CambioEstado):
        self._cambioEstadoActual = nuevoCambioEstadoActual

    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, nuevoEstado : Estado):
        self._estado = nuevoEstado

    @property
    def eventoSismicoId(self):
        return self._eventoSismicoId
    #endregion

    #TODO CHEQUEAR ESTO, NO ESTOY SEGURO DE QUE SE RESUELVA ASÍ
    def sosAutoDetectado(self) -> bool:
        return isinstance(self._estado, AutoDetectado)
    
    def getFechaHoraOcurrencia(self) ->datetime: # jr
        return self._fechaHoraOcurrencia

    def getUbicacion(self) -> list[list[float]]:
        return [self.getCoordenadasEpicentro(), self.getCoordenadasHipocentro()]# TODO CHEQUEAR ESTO CON EL DIAGRAMA

    def getCoordenadasEpicentro(self) -> list[float]:
        return [self.latitudEpicentro, self.longitudEpicentro]
    
    def getCoordenadasHipocentro(self) -> list[float]:
        return [self.latitudHipocentro, self.longitudHipocentro]
    

    # EventoSismico seleccionado

    def revisar(self, analista, fechaHoraActual) -> None:
        self._estado.revisar(analista, fechaHoraActual, self, cambiosEstado=self._cambioEstado)

    def buscarCambioEstadoActual(self) -> None:
        for cambio in self._cambioEstado:
            if cambio.sosActual():
                self._cambioEstadoActual = cambio
        return None


    def actualizarEstadoRechazado(self, analista, fechaHoraActual):
        self._estado.rechazar(analista, fechaHoraActual, self)


    def obtenerDatos(self):
        alcance = self.alcanceSismo.nombre
        clasificacion = self.clasificacionSismo.nombre
        origen = self.origenGeneracion.nombre
        magnitud = self.valorMagnitud

        return {
            "alcanceSismo": alcance,
            "clasificacionSismo": clasificacion,
            "origenGeneracion": origen,
            "valorMagnitud" : magnitud
        }


    def obtenerDatosSerieTemporal(self):
        return [serie.obtenerDatos() for serie in self._seriesTemporales]


    def confirmar(self, analista: AnalistaSismos, fechaHoraActual: datetime) -> None:
        self._estado.confirmar(analista, fechaHoraActual, self)


    def actualizarEstadoPendiente(self, analista, fechaHoraActual) -> None:
        self._estado.actualizarEstadoPendiente(analista, fechaHoraActual, self)


    def obtenerCambioEstadoActual(self):
        self.buscarCambioEstadoActual()
        return self._cambioEstadoActual

    @eventoSismicoId.setter
    def eventoSismicoId(self, value):
        self._eventoSismicoId = value


    def __repr__(self):
        return (f"EventoSismico(fechaHoraOcurrencia={self._fechaHoraOcurrencia}, magnitud={self._magnitudRitcher},"
                f" latitudHipocentro={self._latitudHipocentro}, longitudHipocentro={self._longitudHipocentro},"
                f" estado={self._estado}, alcanceSismo={self._alcanceSismo}, origenGeneracion={self._origenGeneracion},"
                f" clasificacionSismo={self._clasificacionSismo}, latitudEpicentro={self._latitudEpicentro},"
                f" longitudEpicentro={self._longitudEpicentro}, seriesTemporales={self._seriesTemporales})")

    def agregarCambioEstado(self, nuevo_cambio_estado: 'CambioEstado'):
        self._cambioEstado.append(nuevo_cambio_estado)