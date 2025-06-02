from Entitys.AnalistaSismos import AnalistaSismos

class Usuario:
    def __init__(self, nombre: str, contrasena: str, logueado: AnalistaSismos):
        self._nombre = nombre
        self._contrasena = contrasena
        self._logueado = logueado

#region Getters y Setters
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

    @property
    def logueado(self):
        return self._logueado
    @logueado.setter
    def logueado(self, estado: AnalistaSismos):
        self._logueado = estado
#endregion

    def __str__(self):
        return f"Usuario(nombre={self._nombre}, contrasena={self._contrasena}, logueado={self._logueado})"