from Entitys.DetalleMuestraSismica import DetalleMuestraSismica
import datetime

class MuestraSismica:
    def __init__(self, fechaHoraMuestra: datetime, detalleMuestra : DetalleMuestraSismica):
        self._fechaHoraMuestra = fechaHoraMuestra
        self._detalles = [detalleMuestra]

    def agregarDetalle(self, detalle: DetalleMuestraSismica):
        self._detalles.append(detalle)

    def obtenerDatos(self):
        #return [detalle.obtenerDatos() for detalle in self._detalles]
        return {
            "fechaHoraMuestra": self._fechaHoraMuestra,
            "detalles": [detalle.obtenerDatos() for detalle in self._detalles]
        }

    def __repr__(self):
        return f"MuestraSismica(fechaHoraMuestra={self._fechaHoraMuestra}, detalles={self._detalles})"