from Entitys.Estado import Estado

class Cerrado(Estado):
    def __init__(self):
        super().__init__("Cerrado", "EventoSismico")