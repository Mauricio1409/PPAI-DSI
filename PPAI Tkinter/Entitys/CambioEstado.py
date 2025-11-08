from datetime import datetime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Entitys.STATE.Estado import Estado

class CambioEstado:
    def __init__(self, fechaHoraInicio: datetime, estado : 'Estado', analista, fechaHoraFin: datetime = None, cambioEstadoId: int = None):
        self._cambioEstadoId = cambioEstadoId
        self._fechaHoraInicio = fechaHoraInicio
        self._fechaHoraFin = fechaHoraFin
        self._estado = estado
        self._analistaResponsable = analista

#region Getters y Setters
    @property
    def analistaResponsable(self):
        return self._analistaResponsable
    @property
    def cambioEstadoId(self):
        return self._cambioEstadoId
    @property
    def fechaHoraInicio(self):
        return self._fechaHoraInicio

    @fechaHoraInicio.setter
    def fechaHoraInicio(self, value: datetime):
        self._fechaHoraInicio = value

    @property
    def fechaHoraFin(self):
        return self._fechaHoraFin

    @fechaHoraFin.setter
    def fechaHoraFin(self, value: datetime):
        self._fechaHoraFin = value
    @property
    def estado(self):
        return self._estado

#endregion


    def esPendienteRevision(self):
        return self._fechaHoraFin is None


    def sosActual(self):
        return self._fechaHoraFin is None


    def __repr__(self):
        return (f"CambioEstado(fechaHoraInicio={self._fechaHoraInicio}, "
                f"EstadoActual={self._estado.nombre},"
                f"fechaHoraFin={self._fechaHoraFin})")

    @cambioEstadoId.setter
    def cambioEstadoId(self, value):
        self._cambioEstadoId = value
