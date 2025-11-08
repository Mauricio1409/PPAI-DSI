from datetime import datetime

from Entitys.AnalistaSismos import AnalistaSismos
from Entitys.CambioEstado import CambioEstado
from Entitys.STATE.Estado import Estado

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Entitys.EventoSismico import EventoSismico


class AutoDetectado(Estado):
    def __init__(self):
        super().__init__("AUTO_DETECTADO")

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
    def buscarCambioEstadoActual(cambiosDeEstado: list[CambioEstado]) -> CambioEstado | None:
        for cambio in cambiosDeEstado:
            if cambio.sosActual():
                return cambio
        return None
        
    def confirmarRevision(self):
        print("Confirmando revisión del estado AutoDetectado...")
        # Lógica específica para confirmar la revisión del estado
        
        
    