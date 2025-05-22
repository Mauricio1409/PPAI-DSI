class AnalistaSismos:
    def __init__(self, nombre: str, apellido: str, id_analista: int):
        self._nombre = nombre
        self._apellido = apellido
        self._id_analista = id_analista


    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevoNombre: str):
        self._nombre = nuevoNombre
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, nuevoApellido: str):
        self._apellido = nuevoApellido
    @property
    def id_analista(self):
        return self._id_analista
    @id_analista.setter
    def id_analista(self, nuevoId: int):
        self._id_analista = nuevoId