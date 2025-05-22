from Entitys.MuestraSismica import MuestraSismica
import datetime


class SerieTemporal:
    def __init__(self, condicionAlarma: int, fechaHoraInicioRegistroMuestras: datetime, fechaHoraRegistro: datetime, frecuenciaMuestreo: float, muestraSismica : list[MuestraSismica], estacionSismologica = None):
        self._condicionAlarma = condicionAlarma
        self._fechaHoraInicioRegistroMuestras = fechaHoraInicioRegistroMuestras
        self._fechaHoraRegistro = fechaHoraRegistro
        self._frecuenciaMuestreo = frecuenciaMuestreo
        self._muestras = muestraSismica
        self._estacionSimologica = estacionSismologica #TODO esto esta hardcodeado, debería buscar cual es su estación sismológica en la BDD

    def agregarMuestra(self, muestra: MuestraSismica):
        self._muestras.append(muestra)

    def obtenerDatos(self):
        #return [muestra.obtenerDatos() for muestra in self._muestras]
        return {
            "estacionSismologica": self._estacionSimologica,
            "condicionAlarma": self._condicionAlarma,
            "fechaHoraInicioRegistroMuestras": self._fechaHoraInicioRegistroMuestras,
            "fechaHoraRegistro": self._fechaHoraRegistro,
            "frecuenciaMuestreo": self._frecuenciaMuestreo,
            "muestras": [muestra.obtenerDatos() for muestra in self._muestras]
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