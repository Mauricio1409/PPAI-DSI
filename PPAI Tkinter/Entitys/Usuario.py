from Entitys.AnalistaSismos import AnalistaSismos

class Usuario:
    def __init__(self, nombre: str, contrasena: str, logueado: AnalistaSismos):
        self._nombre = nombre
        self._contrasena = contrasena
        self._logueado = logueado

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, value: str):
        self._contrasena = value

    def getLogueado(self):
        return self._logueado

    def setLogueado(self, estado: AnalistaSismos):
        self._logueado = estado

    def __str__(self):
        return f"Usuario(nombre={self._nombre}, contrasena={self._contrasena}, logueado={self._logueado})"