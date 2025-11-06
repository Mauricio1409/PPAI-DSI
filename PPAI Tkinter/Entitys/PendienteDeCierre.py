from Entitys.Estado import Estado

class PendienteDeCierre(Estado):
    def __init__(self):
        super().__init__("Pendiente de Cierre", "EventoSismico")

    def cerrar(self):
        print("Cerrando el evento sísmico...")
        # Lógica para cerrar el evento sísmico