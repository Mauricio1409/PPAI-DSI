from Entitys.STATE.Estado import Estado

class AutoDetectado(Estado):
    def __init__(self):
        super().__init__("AUTO_DETECTADO")
        

    def revisar(self, analista, fechaHoraActual, eventoSismico):
        print("Revisando datos para evento AutoDetectado...")
        # Lógica específica para revisar datos de un evento AutoDetectado
        
    def confirmarRevision(self):
        print("Confirmando revisión del estado AutoDetectado...")
        # Lógica específica para confirmar la revisión del estado
        
        
    