from abc import ABC
from datetime import datetime

from Entitys.CambioEstado import CambioEstado

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Entitys.AnalistaSismos import AnalistaSismos
    from Entitys.EventoSismico import EventoSismico


class Estado(ABC):
    def __init__(self, nombre: str):
        self._nombre: str = nombre

    #region Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevoNombre: str):
        self._nombre = nuevoNombre

    #endregion

    def __str__(self):
        return f"Estado: {self.nombre}"

    def registrarPendienteCierre(self):
        print(f"Operación 'RegistrarPendienteCierre' no permitida en estado: {self.nombre}")
        return False

    def adquirirDatos(self):
        """
        Método para adquirir datos del evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'adquirirDatos' no permitida en estado: {self.nombre}")



    def revisar(self, analista: 'AnalistaSismos', fechaHoraActual: 'datetime', eventoSismico: 'EventoSismico',
                cambiosEstado: list['CambioEstado']) -> None:
        """
        Método para revisar el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'revisar' no permitida en estado: {self.nombre}")


    def confirmarRevision(self):
        """
        Método para confirmar la revisión del evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'confirmarRevision' no permitida en estado: {self.nombre}")


    def registrarAutomatico(self):
        """
        Método para registrar automáticamente el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'registrarAutomatico' no permitida en estado: {self.nombre}")


    def anular(self):
        """
        Método para anular el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'anular' no permitida en estado: {self.nombre}")


    def controlarTiempo(self):
        """
        Método para controlar el tiempo del evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'controlarTiempo' no permitida en estado: {self.nombre}")


    def confirmar(self, analista, fechaHoraActual, eventoSismico):
        """
        Método para confirmar el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'confirmar' no permitida en estado: {self.nombre}")


    def derivar(self):
        """
        Método para derivar el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'derivar' no permitida en estado: {self.nombre}")


    def rechazar(self, analista, fechaHoraActual, eventoSismico):
        """
        Método para rechazar el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'rechazar' no permitida en estado: {self.nombre}")


    def registrarPendientesCierre(self):
        """
        Método para registrar el evento como pendiente de cierre.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'registrarPendientesCierre' no permitida en estado: {self.nombre}")


    def cerrar(self):
        """
        Método para cerrar el evento sísmico.
        Retorna False por defecto indicando que esta operación no está permitida en este estado.
        """
        print(f"Operación 'cerrar' no permitida en estado: {self.nombre}")

    def actualizarEstadoAAutoDetectado(self, analista, fechaHoraActual, eventoSismico):
        print(f"Operacion no soportada en estado: {self.nombre}")

    def actualizarAutomatico(self):
        print(f"Operacion no soportada en estado: {self.nombre}")
        # Lógica específica para actualizar el estado automáticamente

    def __repr__(self):
        return f"(Estado: {self.nombre})"


    @staticmethod
    def cambiarCambioEstado(analista: 'AnalistaSismos', fechaHoraActual: 'datetime',
                            eventoSismico: 'EventoSismico', estado: 'Estado') -> None:
        nuevo_cambio_estado = CambioEstado(fechaHoraActual, estado, analista)
        eventoSismico.agregarCambioEstado(nuevo_cambio_estado)
        print('-' * 100)
        print("cambios de estados realizados hasta acá: ")
        print('-' * 100)
        print('-' * 100)
        for cambio in eventoSismico.cambioEstado:
            print(cambio)
        print('-' * 100)


        eventoSismico._cambioEstadoActual = nuevo_cambio_estado
        print('-' * 100)
        print("cambio de estado actual DESPUÉS DEL CAMBIO: ", eventoSismico.cambioEstadoActual)
        print('-' * 100)