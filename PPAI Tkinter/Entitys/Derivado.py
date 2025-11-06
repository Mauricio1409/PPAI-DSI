from Entitys.Estado import Estado

class Derivado(Estado):
    def __init__(self):
        super().__init__("Derivado", "EventoSismico")
        
        
    def confirmar(self):
        print("Confirmando el estado Derivado...")
        # Lógica específica para confirmar el estado Derivado
        
    def rechazar(self):
        print("Rechazando el estado Derivado...")
        # Lógica específica para rechazar el estado Derivado
        
    