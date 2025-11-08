from Entitys.STATE.Estado import Estado

class Derivado(Estado):
    def __init__(self):
        super().__init__("DERIVADO")
        
        
    def confirmar(self, analista, fechaHoraActual, eventoSismico):
        print("Confirmando el estado Derivado...")
        # Lógica específica para confirmar el estado Derivado
        
    def rechazar(self, analista, fechaHoraActual, eventoSismico):
        print("Rechazando el estado Derivado...")
        # Lógica específica para rechazar el estado Derivado
        
    