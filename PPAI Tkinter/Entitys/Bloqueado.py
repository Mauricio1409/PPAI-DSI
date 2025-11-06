from Entitys.Estado import Estado
from Entitys.Rechazado import Recahazado
from Entitys.CambioEstado import CambioEstado

class Bloqueado(Estado):
    def __init__(self):
        super().__init__("Bloqueado", "EventoSismico")
        
    def confirmar(self):
        """Override: Permite confirmar un evento bloqueado."""
        print("Confirmando el estado Bloqueado...")
        # Lógica específica para confirmar el estado Bloqueado
        # Por ejemplo: cambiar el estado a Confirmado
        return True
        
    def rechazar(self, analista, fechaHoraActual, eventoSismico):
        cambios_estado = eventoSismico.cambioEstado
        # busco el cambio estado actual y le seteo la fechaHoraFin
        for cambio in cambios_estado:
            if cambio.fechaHoraFin is None:
                cambio.fechaHoraFin(fechaHoraActual)
                break
        
        # creo el estado rechazado
        rechazado = Recahazado()
        
        # creo el nuevo cambio de estado
        nuevo_cambio_estado = CambioEstado(
            fechaHoraInicio=fechaHoraActual, 
            estado=rechazado, 
            fechaHoraFin=None, 
            analista=analista
            )
        
        # lo agrego a la lista de cambios de estado del evento sísmico
        cambios_estado.append(nuevo_cambio_estado)
        
        eventoSismico.cambioEstado = cambios_estado
        eventoSismico.estado = rechazado
        
        
            
        
        """Override: Permite rechazar un evento bloqueado."""
        print("Rechazando el estado Bloqueado...")
        # Lógica específica para rechazar el estado Bloqueado
        # Por ejemplo: cambiar el estado a Rechazado
        return True
        
    def derivar(self):
        """Override: Permite derivar un evento bloqueado."""
        print("Derivando el estado Bloqueado...")
        # Lógica específica para derivar el estado Bloqueado
        # Por ejemplo: cambiar el estado a Derivado
        return True
        
    
        
    