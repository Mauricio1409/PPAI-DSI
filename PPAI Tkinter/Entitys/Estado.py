class Estado:
    def __init__(self, nombre: str, ambito : int):
        self._nombre = nombre
        self._ambito = ambito

    def sosPendienteRevision(self):
        if self.ambito == "EventoSismico" and self.nombre == "PendienteRevision":
            return True
        return False

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevoNombre: str):
        self._nombre = nuevoNombre
    @property
    def ambito(self):
        return self._ambito

    @ambito.setter
    def ambito(self, nuevoAmbito : int):
        self._ambito = nuevoAmbito

    def __str__(self):
        return (f"Estado: {self.nombre}")

