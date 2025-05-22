from Entitys.Estado import Estado

class CambioEstado:
    def __init__(self, fechaHoraInicio: int, estado : Estado, fechaHoraFin: int = None):
        self._fechaHoraInicio = fechaHoraInicio
        self._fechaHoraFin = fechaHoraFin
        self._estado = estado

    @property
    def fechaHoraInicio(self):
        return self._fechaHoraInicio

    @fechaHoraInicio.setter
    def fechaHoraInicio(self, value: int):
        self._fechaHoraInicio = value

    @property
    def fechaHoraFin(self):
        return self._fechaHoraFin

    @fechaHoraFin.setter
    def fechaHoraFin(self, value: int):
        self._fechaHoraFin = value

    def esPendienteRevision(self):
        # Implementa la lógica real según tu dominio
        return self._fechaHoraFin is None

    @classmethod
    def new(cls, fechaHoraInicio: int):
        return cls(fechaHoraInicio)

    def setechaHoraFin(self, value: int):
        self._fechaHoraFin = value

    def setFechaHoraFin(self, value: int):
        self._fechaHoraFin = value

    def sosActual(self):
        # Implementa la lógica real según tu dominio
        return self._fechaHoraFin is None

    def __repr__(self):
        return (f"CambioEstado(fechaHoraInicio={self._fechaHoraInicio}, "
                f"fechaHoraFin={self._fechaHoraFin})")