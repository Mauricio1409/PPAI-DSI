from Entitys.STATE.Estado import Estado

class EventoSinRevision(Estado):
    def __init__(self):
        super().__init__("EVENTO_SIN_REVISION")
        
    