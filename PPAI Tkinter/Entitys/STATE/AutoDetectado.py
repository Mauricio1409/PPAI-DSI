from Entitys.STATE.Estado import Estado

class AutoDetectado(Estado):
    def __init__(self):
        super().__init__("AutoDetectado", "EventoSismico")
        

    def revisar(self):
        print("Revisando datos para evento AutoDetectado...")
        # Lógica específica para revisar datos de un evento AutoDetectado
        
    def confirmarRevision(self):
        print("Confirmando revisión del estado AutoDetectado...")
        # Lógica específica para confirmar la revisión del estado
        
        
    