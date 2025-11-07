from Entitys.STATE.Estado import Estado
from datetime import datetime

class CambioEstado:
    def __init__(self, fechaHoraInicio: datetime, estado : Estado, analista, fechaHoraFin: datetime = None):
        self._fechaHoraInicio = fechaHoraInicio
        self._fechaHoraFin = fechaHoraFin
        self._estado = estado
        self._analistaResponsable = analista

#region Getters y Setters
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

#endregion


    def esPendienteRevision(self):
        return self._fechaHoraFin is None


    def sosActual(self):
        return self._fechaHoraFin is None


    def __repr__(self):
        return (f"CambioEstado(fechaHoraInicio={self._fechaHoraInicio}, "
                f"EstadoActual={self._estado.nombre},"
                f"fechaHoraFin={self._fechaHoraFin})")
