from datetime import datetime

from Entitys.EstacionSismologica import EstacionSismologica
class Sismografo:
    def __init__(self, fechaAdquisicion: datetime, numeroSerie: int,
                 estacionSismologica : EstacionSismologica, sismografoId: int = None):
        self._sismografoId = sismografoId
        self._fechaAdquisicion = fechaAdquisicion
        self._numeroSerie = numeroSerie
        self._estacionSismologica = estacionSismologica

# region Getters y Setters
    @property
    def fechaAdquisicion(self):
        return self._fechaAdquisicion

    @fechaAdquisicion.setter
    def fechaAdquisicion(self, value: int):
        self._fechaAdquisicion = value

    @property
    def numeroSerie(self):
        return self._numeroSerie

    @numeroSerie.setter
    def numeroSerie(self, value: int):
        self._numeroSerie = value
        
    @property
    def estacionSismologica(self):
        return self._estacionSismologica
    
    @estacionSismologica.setter
    def estacionSismologica(self, valor):
        self._estacionSismologica = valor
    @property
    def sismografoId(self):
        return self._sismografoId
# endregion

    def __repr__(self):
        return (f"Sismografo(fechaAdquisicion={self._fechaAdquisicion}, "
                f"identificadorSismografo={self._sismografoId}, "
                f"numeroSerie={self._numeroSerie})")