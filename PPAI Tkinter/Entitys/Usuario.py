class Usuario:
    def __init__(self, nombre: int, contrasena: int):
        self._nombre = nombre
        self._contrasena = contrasena
        self._logueado = False

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value: int):
        self._nombre = value

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, value: int):
        self._contrasena = value

    def getLogueado(self):
        return self._logueado

    def setLogueado(self, estado: bool):
        self._logueado = estado

    def __str__(self):
        return f"Usuario(nombre={self._nombre}, contrasena={self._contrasena}, logueado={self._logueado})"