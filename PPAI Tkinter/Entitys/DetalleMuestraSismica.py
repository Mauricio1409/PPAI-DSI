class DetalleMuestraSismica:
    def __init__(self, valor: int):
        self._valor = valor

# region Getters y Setters
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, nuevoValor : int):
         self._valor = nuevoValor
# endregion

    def obtenerDatos(self):
        return {
            "valor": self._valor
        }
    
    def __repr__(self):
        return f"DetalleMuestraSismica(valor={self._valor})"