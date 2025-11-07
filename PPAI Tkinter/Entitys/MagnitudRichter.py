class MagnitudRichter:
    def __init__(self, descripcionMagnitud: str, numero: int, magnitudRichterId: int = None):
        self._magnitudRichterId = magnitudRichterId
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

    @property
    def magnitudRichterId(self):
        return self._magnitudRichterId

    def __repr__(self):
        return f"MagnitudRichter(descripcionMagnitud={self._descripcionMagnitud}, numero={self._numero})"