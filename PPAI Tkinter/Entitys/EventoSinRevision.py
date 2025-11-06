from Entitys.Estado import Estado

class EventoSinRevision(Estado):
    def __init__(self):
        super().__init__("EventoSinRevisión", "EventoSismico")
        
    