class DetalleMuestraSismica:
    def __init__(self, valor: int):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, nuevoValor : int):
         self._valor = nuevoValor

    def __repr__(self):
        return f"DetalleMuestraSismica(valor={self._valor})"

    def obtenerDatos(self):
        return {
            "valor": self._valor
        }