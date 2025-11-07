from Entitys.STATE.Estado import Estado

class Confirmado(Estado):
    def __init__(self):
        super().__init__("Confirmado", "EventoSismico")

    def registrarPendienteCierre(self):
        print("Registrando el evento sísmico como pendiente de cierre...")
        # Lógica para cambiar el estado a PendienteDeCierre

    def adquirirDatos(self):
        print("Adquiriendo datos adicionales del evento sísmico...")
        # Lógica para adquirir datos adicionales
    