from Entitys.DetalleMuestraSismica import DetalleMuestraSismica
import datetime

class MuestraSismica:
    def __init__(self, fechaHoraMuestra: datetime, detalleMuestra : DetalleMuestraSismica):
        self._fechaHoraMuestra = fechaHoraMuestra
        self._detalles = [detalleMuestra]

# region Getters y Setters
    @property
    def fechaHoraMuestra(self):
        return self._fechaHoraMuestra
    @fechaHoraMuestra.setter
    def fechaHoraMuestra(self, valor: datetime):
        self._fechaHoraMuestra = valor

    @property
    def detalles(self):
        return self._detalles   
    @detalles.setter
    def detalles(self, valor):
        self._detalles = valor
# endregion

    def obtenerDatos(self):
        #return [detalle.obtenerDatos() for detalle in self._detalles]
        return {
            "fechaHoraMuestra": self._fechaHoraMuestra,
            "detalles": [detalle.obtenerDatos() for detalle in self._detalles]
        }

    def __repr__(self):
        return f"MuestraSismica(fechaHoraMuestra={self._fechaHoraMuestra}, detalles={self._detalles})"
    
    #TODO: metodos de implementación fuera del diagrama
    def agregarDetalle(self, detalle: DetalleMuestraSismica):
        self._detalles.append(detalle)