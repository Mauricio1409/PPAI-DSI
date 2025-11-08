from datetime import datetime

from Entitys.AnalistaSismos import AnalistaSismos
from Entitys.STATE.Confirmado import Confirmado
from Entitys.STATE.Estado import Estado
from Entitys.STATE.Rechazado import Rechazado
from Entitys.CambioEstado import CambioEstado

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Entitys.EventoSismico import EventoSismico
    from Entitys.STATE.PendienteDeRevision import PendienteDeRevision


class Bloqueado(Estado):
    def __init__(self):
        super().__init__("BLOQUEADO")
        
    def confirmar(self, analista, fechaHoraActual, eventoSismico):
        cambioDeEstado = eventoSismico.cambioEstado

        cambioEstadoActualEventoSismico = self.obtenerCambioEstadoActual(cambioDeEstado)
        cambioEstadoActualEventoSismico.fechaHoraFin = fechaHoraActual

        estadoConfirmado = Confirmado()

        self.cambiarCambioEstado(analista, fechaHoraActual, eventoSismico, estadoConfirmado)

        eventoSismico.estado = estadoConfirmado
        
    def rechazar(self, analista, fechaHoraActual, eventoSismico):
        cambiosDeEstado = eventoSismico.cambioEstado

        # busco el cambio estado actual y le seteo la fechaHoraFin
        cambioEstadoActualEventoSismico = self.obtenerCambioEstadoActual(cambiosDeEstado)
        cambioEstadoActualEventoSismico.fechaHoraFin = fechaHoraActual

        # creo el estado rechazado
        rechazado = Rechazado()

        self.cambiarCambioEstado(analista, fechaHoraActual, eventoSismico, rechazado)

        eventoSismico.estado = rechazado
        
    def derivar(self):
        """Override: Permite derivar un evento bloqueado."""
        print("Derivando el estado Bloqueado...")
        # Lógica específica para derivar el estado Bloqueado
        # Por ejemplo: cambiar el estado a Derivado
        return True

    def actualizarEstadoPendiente(self, analista, fechaHoraActual, eventoSismico):

        from Entitys.STATE.PendienteDeRevision import PendienteDeRevision
        # ATENCIÓN, este import DEBE estar OBLIGATORIAMENTE acá, si lo ponemos al inicio del archivo genera
        # un circular import exception

        cambioDeEstado = eventoSismico.cambioEstado
        cambioEstadoActualEventoSismico = self.obtenerCambioEstadoActual(cambioDeEstado)

        cambioEstadoActualEventoSismico.fechaHoraFin = fechaHoraActual

        estadoPendiente = PendienteDeRevision()

        self.cambiarCambioEstado(analista, fechaHoraActual, eventoSismico, estadoPendiente)

        eventoSismico.estado = estadoPendiente


    @staticmethod
    def obtenerCambioEstadoActual(cambiosDeEstado: list[CambioEstado]):
        for cambio in cambiosDeEstado:
            if cambio.sosActual():
                return cambio

