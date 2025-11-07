from Entitys.tipoDato import TipoDato

class DetalleMuestraSismica:
    def __init__(self, valor: float, tipo: TipoDato, detalleMuestraId: int = None):
        self._detalleMuestraId = detalleMuestraId
        self._valor = valor
        self.tipo = tipo

    # region Getters y Setters
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, nuevoValor: int):
        self._valor = nuevoValor

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevoTipo: TipoDato):
        self._tipo = nuevoTipo

    @property
    def detalleMuestraId(self):
        return self._detalleMuestraId
    # endregion

    def obtenerDatos(self):
        return {
            "valor": self._valor,
            "tipo": self._tipo.denominacion
        }

    def __repr__(self):
        return f"DetalleMuestraSismica(valor={self._valor})"