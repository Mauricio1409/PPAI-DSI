class OrigenDeGeneracion:
    def __init__(self, descripcion: int, nombre: int):
        self._descripcion = descripcion
        self._nombre = nombre

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: int):
        self._descripcion = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value: int):
        self._nombre = value

    def getNombre(self):
        nombre = nombre()
        return nombre

    def obtenerOrigen(self):
        return {
            "descripcion": self._descripcion,
            "nombre": self._nombre
        }

    def __repr__(self):
        return f"OrigenDeGeneracion(descripcion={self._descripcion}, nombre={self._nombre})"