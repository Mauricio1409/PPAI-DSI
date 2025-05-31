from Entitys.TipoDeDato import TipoDeDato

class DetalleMuestraSismica:
    def __init__(self, valor: int, tipoDato: TipoDeDato):
        self._valor = valor
        self._tipoDato = tipoDato

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