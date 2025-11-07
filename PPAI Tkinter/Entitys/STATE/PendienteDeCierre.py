from Entitys.STATE.Estado import Estado

class PendienteDeCierre(Estado):
    def __init__(self):
        super().__init__("PENDIENTE_DE_CIERRE")

    def cerrar(self):
        print("Cerrando el evento sísmico...")
        # Lógica para cerrar el evento sísmico