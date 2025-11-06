from Entitys.Estado import Estado

class PendienteDeRevision(Estado):
    def __init__(self):
        super().__init__("Pendiente de Revisión", "EventoSismico")
        
        
    def anular(self):
        print("Anulando el evento sísmico...")
        # Lógica para anular el evento sísmico
        
    def controlarTiempo(self):
        print("Controlando el tiempo para el estado Pendiente de Revisión...")
        # Lógica para controlar el tiempo en este estado
        
    def revisar(self):
        print("Revisando datos para evento Pendiente de Revisión...")
        # Lógica específica para revisar datos de un evento Pendiente de Revisión