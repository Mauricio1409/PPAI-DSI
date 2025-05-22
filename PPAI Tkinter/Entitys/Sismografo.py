from Entitys.EstacionSismologica import EstacionSismologica
class Sismografo:
    def __init__(self, fechaAdquisicion: int, identificadorSismografo: int, numeroSerie: int, estacionSismologica : EstacionSismologica):
        self._fechaAdquisicion = fechaAdquisicion
        self._identificadorSismografo = identificadorSismografo
        self._numeroSerie = numeroSerie
        self._estacionSismologica = estacionSismologica

    @property
    def fechaAdquisicion(self):
        return self._fechaAdquisicion

    @fechaAdquisicion.setter
    def fechaAdquisicion(self, value: int):
        self._fechaAdquisicion = value

    @property
    def identificadorSismografo(self):
        return self._identificadorSismografo

    @identificadorSismografo.setter
    def identificadorSismografo(self, value: int):
        self._identificadorSismografo = value

    @property
    def numeroSerie(self):
        return self._numeroSerie

    @numeroSerie.setter
    def numeroSerie(self, value: int):
        self._numeroSerie = value

    def esTuSerie(self, serie: int):
        return self._numeroSerie == serie

    def __repr__(self):
        return (f"Sismografo(fechaAdquisicion={self._fechaAdquisicion}, "
                f"identificadorSismografo={self._identificadorSismografo}, "
                f"numeroSerie={self._numeroSerie})")