from Entitys.MuestraSismica import MuestraSismica
from Entitys.Sismografo import Sismografo
from datetime import datetime


class SerieTemporal:
    def __init__(self, condicionAlarma: int, fechaHoraInicioRegistroMuestras: datetime, fechaHoraRegistro: datetime, frecuenciaMuestreo: float, muestraSismica : list[MuestraSismica], sismografo : Sismografo):
        self._condicionAlarma: int = condicionAlarma
        self._fechaHoraInicioRegistroMuestras: datetime = fechaHoraInicioRegistroMuestras
        self._fechaHoraRegistro: datetime = fechaHoraRegistro
        self._frecuenciaMuestreo = frecuenciaMuestreo
        self._muestras = muestraSismica
        self._sismografo = sismografo #TODO esto esta hardcodeado, debería buscar cual es su estación sismológica en la BDD

    # region Getters y Setters
    @property
    def condicionAlarma(self):
        return self._condicionAlarma
    
    @condicionAlarma.setter
    def condicionAlarma(self, valor : int):
        self._condicionAlarma = valor
        
    @property
    def fechaHoraInicioRegistroMuestras(self):
        return self._fechaHoraInicioRegistroMuestras

    @fechaHoraInicioRegistroMuestras.setter
    def fechaHoraInicioRegistroMuestras(self, valor):
        self._fechaHoraInicioRegistroMuestras = valor

    @property
    def fechaHoraRegistro(self):
        return self._fechaHoraRegistro

    @fechaHoraRegistro.setter
    def fechaHoraRegistro(self, valor):
        self._fechaHoraRegistro = valor

    @property
    def frecuenciaMuestreo(self):
        return self._frecuenciaMuestreo

    @frecuenciaMuestreo.setter
    def frecuenciaMuestreo(self, valor):
        self._frecuenciaMuestreo = valor

    @property
    def muestras(self):
        return self._muestras

    @muestras.setter
    def muestras(self, valor):
        self._muestras = valor

    @property
    def sismografo(self):
        return self._sismografo

    @sismografo.setter
    def sismografo(self, valor):
        self._sismografo = valor
    # endregion

    def obtenerDatos(self):
        return {
            "estacionSismologica": self.sismografo.estacionSismologica,
            "muestras": [muestra.obtenerDatos() for muestra in self.muestras]
        }

    '''
    def __repr__(self):
        return (f"SerieTemporal(condicionAlarma={self._condicionAlarma}, "
                f"fechaHoraInicioRegistroMuestras={self._fechaHoraInicioRegistroMuestras}, "
                f"fechaHoraRegistro={self._fechaHoraRegistro}, "
                f"frecuenciaMuestreo={self._frecuenciaMuestreo}, "
                f"muestras={self._muestras})")
    '''

