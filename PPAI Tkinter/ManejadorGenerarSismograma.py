class ManejadorGenerarSismograma:

    def __init__(self, serieTemporal):
        self.rutaSismograma = "recursos/sismograma.png"
        self.datosSerieTemporal = serieTemporal

    def generarSismograma(self):
        return self.rutaSismograma