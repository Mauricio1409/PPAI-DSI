class AlcanceSismo:
    def __init__(self, descripcion: str, nombre: str):
        self._descripcion = descripcion
        self._nombre = nombre

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


    def obtenerAlcance(self):
        return {
            "descripcion": self._descripcion,
            "nombre": self._nombre
        }

    def __repr__(self):
        return f"AlcanceSismo(descripcion={self._descripcion}, nombre={self._nombre})"