class MagnitudRichter:
    def __init__(self, descripcionMagnitud: int, numero: int):
        self._descripcionMagnitud = descripcionMagnitud
        self._numero = numero

    @property
    def descripcionMagnitud(self):
        return self._descripcionMagnitud

    @descripcionMagnitud.setter
    def descripcionMagnitud(self, value: int):
        self._descripcionMagnitud = value

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value: int):
        self._numero = value

    def __repr__(self):
        return f"MagnitudRichter(descripcionMagnitud={self._descripcionMagnitud}, numero={self._numero})"