from Entitys.MuestraSismica import MuestraSismica
from Entitys.Sismografo import Sismografo
import datetime


class SerieTemporal:
    def __init__(self, condicionAlarma: int, fechaHoraInicioRegistroMuestras: datetime, fechaHoraRegistro: datetime, frecuenciaMuestreo: float, muestraSismica : list[MuestraSismica], sismografo : Sismografo):
        self._condicionAlarma = condicionAlarma
        self._fechaHoraInicioRegistroMuestras = fechaHoraInicioRegistroMuestras
        self._fechaHoraRegistro = fechaHoraRegistro
        self._frecuenciaMuestreo = frecuenciaMuestreo
        self._muestras = muestraSismica
        self._sismografo = sismografo #TODO esto esta hardcodeado, debería buscar cual es su estación sismológica en la BDD

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

    def agregarMuestra(self, muestra: MuestraSismica):
        self._muestras.append(muestra)

    def obtenerDatos(self):
        #return [muestra.obtenerDatos() for muestra in self._muestras]
        '''
        return {
            "estacionSismologica": self.sismografo.estacionSismologica,
            "condicionAlarma": self.condicionAlarma,
            "fechaHoraInicioRegistroMuestras": self.fechaHoraInicioRegistroMuestras,
            "fechaHoraRegistro": self.fechaHoraRegistro,
            "frecuenciaMuestreo": self.frecuenciaMuestreo,
            "muestras": [muestra.obtenerDatos() for muestra in self.muestras]
        }
        '''

        # TODO que estamos haciendo aca??????, el enunciado solo pide que busquemos 3 datos, no todos los datos de la serie temporal

        return {
            "estacionSismologica": self.sismografo.estacionSismologica.codigoEstacion,
            "muestras": [muestra.obtenerDatos() for muestra in self.muestras],
        }


    def sosSerie(self):
        #TODO que es esto?
        return True

    def __repr__(self):
        return (f"SerieTemporal(condicionAlarma={self._condicionAlarma}, "
                f"fechaHoraInicioRegistroMuestras={self._fechaHoraInicioRegistroMuestras}, "
                f"fechaHoraRegistro={self._fechaHoraRegistro}, "
                f"frecuenciaMuestreo={self._frecuenciaMuestreo}, "
                f"muestras={self._muestras})")