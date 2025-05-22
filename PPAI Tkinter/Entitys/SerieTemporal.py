from Entitys.MuestraSismica import MuestraSismica

class SerieTemporal:
    def __init__(self, condicionAlarma: int, fechaHoraInicioRegistroMuestras: int, fechaHoraRegistro: int, frecuenciaMuestreo: int, muestraSismica : MuestraSismica):
        self._condicionAlarma = condicionAlarma
        self._fechaHoraInicioRegistroMuestras = fechaHoraInicioRegistroMuestras
        self._fechaHoraRegistro = fechaHoraRegistro
        self._frecuenciaMuestreo = frecuenciaMuestreo
        self._muestras = [MuestraSismica]

    def agregarMuestra(self, muestra: MuestraSismica):
        self._muestras.append(muestra)

    def obtenerDatos(self):
        return [muestra.obtenerDatos() for muestra in self._muestras]

    def sosSerie(self):
        
        return True

    def __repr__(self):
        return (f"SerieTemporal(condicionAlarma={self._condicionAlarma}, "
                f"fechaHoraInicioRegistroMuestras={self._fechaHoraInicioRegistroMuestras}, "
                f"fechaHoraRegistro={self._fechaHoraRegistro}, "
                f"frecuenciaMuestreo={self._frecuenciaMuestreo}, "
                f"muestras={self._muestras})")