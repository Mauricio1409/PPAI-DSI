from datetime import datetime

class EstacionSismologica:
    def __init__(
        self,
        codigoEstacion: int,
        documentoCertificacionAdq: int,
        fechaSolicitudCertificacion: datetime,
        latitud: float,
        longitud: float,
        nombre: str,
        numeroCertificacionAdquisicion: int,
        estacionSismologicaId: int | None = None
    ):
        self._estacionSismologicaId = estacionSismologicaId
        self._codigoEstacion = codigoEstacion
        self._documentoCertificacionAdq = documentoCertificacionAdq
        self._fechaSolicitudCertificacion = fechaSolicitudCertificacion
        self._latitud = latitud
        self._longitud = longitud
        self._nombre = nombre
        self._numeroCertificacionAdquisicion = numeroCertificacionAdquisicion

#region Getters y Setters
    @property
    def codigoEstacion(self):
        return self._codigoEstacion

    @codigoEstacion.setter
    def codigoEstacion(self, value: int):
        self._codigoEstacion = value

    @property
    def documentoCertificacionAdq(self):
        return self._documentoCertificacionAdq

    @documentoCertificacionAdq.setter
    def documentoCertificacionAdq(self, value: int):
        self._documentoCertificacionAdq = value

    @property
    def fechaSolicitudCertificacion(self):
        return self._fechaSolicitudCertificacion

    @fechaSolicitudCertificacion.setter
    def fechaSolicitudCertificacion(self, value: int):
        self._fechaSolicitudCertificacion = value

    @property
    def latitud(self):
        return self._latitud

    @latitud.setter
    def latitud(self, value: int):
        self._latitud = value

    @property
    def longitud(self):
        return self._longitud

    @longitud.setter
    def longitud(self, value: int):
        self._longitud = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value: int):
        self._nombre = value

    @property
    def numeroCertificacionAdquisicion(self):
        return self._numeroCertificacionAdquisicion

    @numeroCertificacionAdquisicion.setter
    def numeroCertificacionAdquisicion(self, value: int):
        self._numeroCertificacionAdquisicion = value

    @property
    def estacionSismologicaId(self):
        return self._estacionSismologicaId
#endregion


    def getDatos(self):
        return {
            "codigoEstacion": self._codigoEstacion,
            "documentoCertificacionAdq": self._documentoCertificacionAdq,
            "fechaSolicitudCertificacion": self._fechaSolicitudCertificacion,
            "latitud": self._latitud,
            "longitud": self._longitud,
            "nombre": self._nombre,
            "numeroCertificacionAdquisicion": self._numeroCertificacionAdquisicion
        }


    def __repr__(self):
        return (
            f"EstacionSismologica(codigoEstacion={self._codigoEstacion}, "
            f"documentoCertificacionAdq={self._documentoCertificacionAdq}, "
            f"fechaSolicitudCertificacion={self._fechaSolicitudCertificacion}, "
            f"latitud={self._latitud}, longitud={self._longitud}, "
            f"nombre={self._nombre}, "
            f"numeroCertificacionAdquisicion={self._numeroCertificacionAdquisicion})"
        )

    @estacionSismologicaId.setter
    def estacionSismologicaId(self, value):
        self._estacionSismologicaId = value