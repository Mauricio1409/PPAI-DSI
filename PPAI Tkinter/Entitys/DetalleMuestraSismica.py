class DetalleMuestraSismica:
    def __init__(self, valor: float):
        self._valor = valor

# region Getters y Setters
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, nuevoValor : int):
         self._valor = nuevoValor
# endregion

    
    def __repr__(self):
        return f"DetalleMuestraSismica(valor={self._valor})"