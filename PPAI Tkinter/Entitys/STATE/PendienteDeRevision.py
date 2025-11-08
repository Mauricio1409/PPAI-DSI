from datetime import datetime

from Entitys.AnalistaSismos import AnalistaSismos
from Entitys.CambioEstado import CambioEstado
from Entitys.STATE.Estado import Estado

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Entitys.EventoSismico import EventoSismico
    from Entitys.STATE.Bloqueado import Bloqueado

class PendienteDeRevision(Estado):
    def __init__(self):
        super().__init__("PENDIENTE_DE_REVISION")
        
        
    def anular(self):
        print("Anulando el evento sísmico...")
        # Lógica para anular el evento sísmico
        
    def controlarTiempo(self):
        print("Controlando el tiempo para el estado Pendiente de Revisión...")
        # Lógica para controlar el tiempo en este estado
        
    def revisar(self, analista: AnalistaSismos, fechaHoraActual: datetime, eventoSismico: 'EventoSismico',
                cambiosEstado: list[CambioEstado]) -> None:
        from Entitys.STATE.Bloqueado import Bloqueado
        # ATENCIÓN, este import DEBE estar OBLIGATORIAMENTE acá, si lo ponemos al inicio del archivo genera
        # un circular import exception

        cambioEstadoEventoSismico = self.buscarCambioEstadoActual(cambiosEstado)
        cambioEstadoEventoSismico.fechaHoraFin = fechaHoraActual
        estadoBloqueado = Bloqueado()
        self.cambiarCambioEstado(analista, fechaHoraActual, eventoSismico, estadoBloqueado)
        eventoSismico.estado = estadoBloqueado

    @staticmethod
    def buscarCambioEstadoActual(cambiosDeEstado: list[CambioEstado]) -> CambioEstado|None:
        for cambio in cambiosDeEstado:
            if cambio.sosActual():
                return cambio
        return None

