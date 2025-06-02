class ClasificacionSismo:
    def __init__(self, kmProfundidadDesde: int, kmProfundidadHasta: int, nombre: str):
        self._kmProfundidadDesde = kmProfundidadDesde
        self._kmProfundidadHasta = kmProfundidadHasta
        self._nombre = nombre

# region Getters y Setters
    @property
    def kmProfundidadDesde(self):
        return self._kmProfundidadDesde

    @kmProfundidadDesde.setter
    def kmProfundidadDesde(self, value: int):
        self._kmProfundidadDesde = value

    @property
    def kmProfundidadHasta(self):
        return self._kmProfundidadHasta

    @kmProfundidadHasta.setter
    def kmProfundidadHasta(self, value: int):
        self._kmProfundidadHasta = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value
# endregion


    def obtenerClasificaicion(self):
        return {
            "kmProfundidadDesde": self._kmProfundidadDesde,
            "kmProfundidadHasta": self._kmProfundidadHasta,
            "nombre": self._nombre
        }

    def __repr__(self):
        return (f"ClasificacionSismo(kmProfundidadDesde={self._kmProfundidadDesde}, "
                f"kmProfundidadHasta={self._kmProfundidadHasta}, nombre={self._nombre})")