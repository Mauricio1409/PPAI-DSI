from datetime import datetime

from Entitys.AnalistaSismos import AnalistaSismos
from Entitys.CambioEstado import CambioEstado
from Entitys.STATE.Estado import Estado

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Entitys.STATE.EventoSismico import EventoSismico
    from Entitys.STATE.Bloqueado import Bloqueado

class PendienteDeRevision(Estado):
    def __init__(self):
        super().__init__("Pendiente de Revisión", "EventoSismico")
        
        
    def anular(self):
        print("Anulando el evento sísmico...")
        # Lógica para anular el evento sísmico
        
    def controlarTiempo(self):
        print("Controlando el tiempo para el estado Pendiente de Revisión...")
        # Lógica para controlar el tiempo en este estado
        
    def revisar(self, analista: AnalistaSismos, fechaHoraActual: datetime, eventoSismico: 'EventoSismico') -> None:
        from Entitys.STATE.Bloqueado import Bloqueado
        # ATENCIÓN, este import DEBE estar OBLIGATORIAMENTE acá, si lo ponemos al inicio del archivo genera
        # un circular import exception

        cambioEstadoEventoSismico = eventoSismico.obtenerCambioEstadoActual()
        cambioEstadoEventoSismico.fechaHoraFin = fechaHoraActual
        estadoBloqueado = Bloqueado()
        self.cambiarCambioEstado(analista, fechaHoraActual, eventoSismico, estadoBloqueado)
        eventoSismico.estado = estadoBloqueado


    @staticmethod
    def cambiarCambioEstado(analista: AnalistaSismos, fechaHoraActual: datetime,
                            eventoSismico: 'EventoSismico', estado: Estado) -> None:

        nuevo_cambio_estado = CambioEstado(fechaHoraActual, estado, analista)
        eventoSismico._cambioEstado.append(nuevo_cambio_estado)
        print('-' * 50)
        print("cambios de estados realizados hasta acá: ", eventoSismico.cambioEstado)
        print('-' * 50)

        print('-' * 50)
        print("cambio de estado actual ANTES DEL CAMBIO: ", eventoSismico.cambioEstadoActual)
        print('-' * 50)

        eventoSismico._cambioEstadoActual = nuevo_cambio_estado
        print('-' * 50)
        print("cambio de estado actual DESPUÉS DEL CAMBIO: ", eventoSismico.cambioEstadoActual)
        print('-' * 50)