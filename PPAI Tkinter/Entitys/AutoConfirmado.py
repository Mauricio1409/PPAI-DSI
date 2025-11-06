from Entitys.Estado import Estado


class AutoConfirmado(Estado):
    def __init__(self):
        super().__init__("AutoConfirmado", "EventoSismico")
        
    def adquirirDatos(self):
        print("Adquiriendo datos para evento AutoDetectado...")
        # Lógica específica para adquirir datos de un evento AutoDetectado
        
    def actualizarAutomatico(self):
        print("Actualizando estado AutoDetectado automáticamente...")
        # Lógica específica para actualizar el estado automáticamente