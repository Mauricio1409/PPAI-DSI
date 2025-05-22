from Entitys.DetalleMuestraSismica import DetalleMuestraSismica

class MuestraSismica:
    def __init__(self, fechaHoraMuestra: int, detalleMuestra : DetalleMuestraSismica):
        self._fechaHoraMuestra = fechaHoraMuestra
        self._detalles = [detalleMuestra]

    def agregarDetalle(self, detalle: DetalleMuestraSismica):
        self._detalles.append(detalle)

    def obtenerDatos(self):
        return [detalle.obtenerDatos() for detalle in self._detalles]

    def __repr__(self):
        return (f"MuestraSismica(fechaHoraMuestra={self._fechaHoraMuestra}, detalles={self._detalles})")