class TipoDeDato:
    def __init__(self, denominacion: str, nombreUnidadMedida: str, valor_umbral: float):
        self._denominacion = denominacion
        self._nombreUnidadMedida = nombreUnidadMedida
        self._valorUmbral = valor_umbral

    @property
    def denominacion(self):
        return self._denominacion
    @denominacion.setter
    def denominacion(self, nuevoValor: int):
        self._denominacion = nuevoValor

    @property
    def nombreUnidadMedida(self):
        return self._nombreUnidadMedida
    @nombreUnidadMedida.setter
    def nombreUnidadMedida(self, nuevoValor: str):
        self._nombreUnidadMedida = nuevoValor

    @property
    def valorUmbral(self):
        return self.valorUmbral
    @valorUmbral.setter
    def valorUmbral(self, nuevoValor: float):
        self._valorUmbral = nuevoValor
