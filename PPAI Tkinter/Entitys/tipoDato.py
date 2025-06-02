class TipoDato:
    def __init__(self, denominacion : str, nombreUnidadMedida :str, valorUmbral : float):
        self._denominacion = denominacion
        self._nombreUnidadMedida = nombreUnidadMedida
        self._valorUmbral = valorUmbral

    # region Getters y Setters
    @property
    def denominacion(self):
        return self._denominacion
    @denominacion.setter
    def denominacion(self, nuevoDenominacion: str):
        self._denominacion = nuevoDenominacion

    @property
    def nombreUnidadMedida(self):
        return self._nombreUnidadMedida
    @nombreUnidadMedida.setter
    def nombreUnidadMedida(self, nuevoNombreUnidadMedida: str):
        self._nombreUnidadMedida = nuevoNombreUnidadMedida

    @property
    def valorUmbral(self):
        return self._valorUmbral
    @valorUmbral.setter
    def valorUmbral(self, nuevoValorUmbral: float):
        self._valorUmbral = nuevoValorUmbral
    # endregion

