class OrigenDeGeneracion:
    def __init__(self, descripcion: str, nombre: str, origenDeGeneracionId: int = None):
        self._origenDeGeneracionId = origenDeGeneracionId
        self._descripcion = descripcion
        self._nombre = nombre

# region Getters y Setters
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: str):
        self._descripcion = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def origenDeGeneracionId(self):
        return self._origenDeGeneracionId
# endregion

    def obtenerDatos(self):
        return {
            "descripcion": self._descripcion,
            "nombre": self._nombre
        }

    def __repr__(self):
        return f"OrigenDeGeneracion(descripcion={self._descripcion}, nombre={self._nombre})"