from Entitys.Usuario import Usuario
from datetime import datetime

class Sesion:
    def __init__(self, sesion_id: str, usuario: Usuario, fechaHoraInicio: datetime, fechaHoraFin: datetime):
        self._sesion_id = sesion_id
        self._usuario = usuario
        self._fechaHoraInicio = fechaHoraInicio
        self._fechaHoraFin = fechaHoraFin

    def obtenerUsuario(self):
        return self._usuario.getLogueado()

    @property
    def sesion_id(self):
        return self._sesion_id

    @property
    def usuario(self):
        return self._usuario

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

    def __repr__(self):
        return (f"Sesion(sesion_id={self._sesion_id}, usuario={self._usuario}, "
                f"fechaHoraInicio={self._fechaHoraInicio}, fechaHoraFin={self._fechaHoraFin})")