from datetime import datetime

from Entitys.AnalistaSismos import AnalistaSismos
from Entitys.EventoSismico import EventoSismico
from Entitys.Sesion import Sesion
from CasoUso.ManejadorGenerarSismograma import ManejadorGenerarSismograma

from infrastructure.database.repositories.EventoSismicoRepository import EventoSismicoRepository
from infrastructure.database.repositories.SesionRepository import SesionRepository

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Boundarys.PantNuevoEventoSismico import VentanaPantNuevoEventoSismico

class ManejadorNuevoEventoSismico:

    def __init__(self, punteroPantalla: 'VentanaPantNuevoEventoSismico',):

        self.punteroPantalla: 'VentanaPantNuevoEventoSismico' = punteroPantalla

        repoEventoSismico = EventoSismicoRepository()
        self.eventosSismicos: list[EventoSismico] = repoEventoSismico.get_all()

        repoSesion = SesionRepository()
        self.sesion: Sesion = repoSesion.get_actual()

        self.eventosPendienteRevision: list[EventoSismico] = []
        self.arrayDatos = []

        self.CasoUsoSismograma = None
        self.datosModificados = False # todo check this
        self.ValorMagnitudMod = None
        self.origenGeneracionMod = None
        self.alcanceMod = None
        self.datosSerieTemporal: list[dict]| None = None
        self.eventoSismicoSeleccionadoActual: EventoSismico|None = None
        self.eventoBloqueado = None
        self.fechaHoraActual: datetime|None = None
        self.analistaLogueado: AnalistaSismos|None = None
        self.datosEventoSismico: dict|None = None

    def registrarNuevaRevision(self):
        self.buscarEventosAutoDetectados()
        self.ordenarPorFechaHora()
        self.punteroPantalla.presentarEventosNoRevisados(self.arrayDatos)

    def buscarEventosAutoDetectados(self):
        self.arrayDatos = []
        for evento in self.eventosSismicos:
            datos_evento = {}
            if evento.sosAutoDetectado():
                datos_evento['evento'] = evento
                datos_evento['fechaHoraOcurrencia'] = evento.fechaHoraOcurrencia
                datos_evento['ubicacion'] = evento.getUbicacion()
                datos_evento['valorMagnitud'] = evento.valorMagnitud

                self.arrayDatos.append(datos_evento)

    def ordenarPorFechaHora(self):
            self.arrayDatos.sort(key = lambda datosEvento : datosEvento['fechaHoraOcurrencia'], reverse=True)


    def eventoSismicoSeleccionado(self, index):
        print(f"Se selecciono el evento sismico en el indice {index}, es el objeto {self.arrayDatos[index].get('evento')}")
        self.eventoSismicoSeleccionadoActual: EventoSismico = self.arrayDatos[index].get('evento')
        self.actualizarEventoABloqueado(self.eventoSismicoSeleccionadoActual)
        self.buscarDatosEvento(self.eventoSismicoSeleccionadoActual)
        self.clasificarPorEstacion()
        for clavedato, dato in self.datosEventoSismico.items(): #todo esto lo hice simplemente para ver que funcionase y recuperase los datos que se necesitan
            print(f"{clavedato}: {dato}")
        ruta_sismo =  self.generarSismograma(self.datosSerieTemporal)
        self.punteroPantalla.mostrarDetallesEvento(self.datosEventoSismico["clasificacionSismo"], ruta_sismo)
        self.punteroPantalla.mostrarOpcionMapa()

    def actualizarEventoABloqueado(self, eventoSismico: EventoSismico):
        self.buscarUsuarioLogueado()
        self.getFechaHora()
        eventoSismico.revisar(self.analistaLogueado, self.fechaHoraActual)
        repoEventoSismico = EventoSismicoRepository()
        #Guardar los cambios realizados al evento sismico (incluye guardar el estado y los nuevos cambioEstado)
        self.eventoSismicoSeleccionadoActual=repoEventoSismico.update(eventoSismico)

    def buscarUsuarioLogueado(self):
        self.analistaLogueado = self.sesion.obtenerUsuario()

    def getFechaHora(self):
        self.fechaHoraActual= datetime.now()



    def buscarDatosEvento(self, evento: EventoSismico):
        self.datosEventoSismico = evento.obtenerDatos()
        self.datosSerieTemporal = evento.obtenerDatosSerieTemporal()
        print("----------------------------------")
        print("DATOS EVENTO SISMICO")
        print(self.datosEventoSismico)
        print("----------------------------------")
        print("DATOS SERIE TEMPORAL")
        print(self.datosSerieTemporal)


    def clasificarPorEstacion(self):
        
        self.datosSerieTemporal.sort(key= lambda Datos : Datos['estacionSismologica'].codigoEstacion)


    def generarSismograma(self, datosSerieTemporal):
        self.CasoUsoSismograma = ManejadorGenerarSismograma(datosSerieTemporal)
        ruta_sismograma = self.CasoUsoSismograma.generarSismograma()
        return ruta_sismograma


    def noVisualizarSeleccionado(self):

        self.punteroPantalla.habilitarEdicionDatos()

        self.punteroPantalla.habilitarEdicionMagnitud(self.datosEventoSismico['valorMagnitud'])
        self.punteroPantalla.habilitarEdicionOrigen(self.datosEventoSismico['origenGeneracion'])
        self.punteroPantalla.habilitarEdicionAlcance(self.datosEventoSismico['alcanceSismo'])

        self.punteroPantalla.habilitarSelectorOpciones()


    def tomarOptGrilla(self, opcion, alcanceSismo, origenGeneracion, valorMagnitud, modifico):

        if self.validarExistenciaMagnitudAlcanceOrigen(valorMagnitud, alcanceSismo, origenGeneracion):

            if modifico:
                self.eventoSismicoSeleccionadoActual.valorMagnitud = valorMagnitud
                self.eventoSismicoSeleccionadoActual.alcanceSismo.nombre = alcanceSismo
                self.eventoSismicoSeleccionadoActual.origenGeneracion.nombre = origenGeneracion
                print('-'*100)
                print("Datos modificados correctamente")
                print("Nuevos datos del Evento Sismico:")
                print(self.eventoSismicoSeleccionadoActual)
                print('-'*100)


            if opcion == "Confirmar Evento":
                self.actualizarEstadoAConfirmado()
                self.finCasoDeUso()

            elif opcion == "Rechazar Evento":

                self.ActualizarEventoARechazado()
                self.finCasoDeUso()

            elif opcion == "Solicitar Revisión a Experto":
                # TODO Lógica para solicitar revisión
                print("Revision Solicitada")
        else:
            print("No se tienen los datos necesarios del evento sismico.")

    def ActualizarEventoARechazado(self):
        self.getFechaHora()
        self.eventoSismicoSeleccionadoActual.actualizarEstadoRechazado(self.analistaLogueado, self.fechaHoraActual)
        print('-'*100)
        print("evento rechazado")
        print('-'*100)
        repoEventoSismico = EventoSismicoRepository()
        # Guardar los cambios realizados al evento sismico (incluye guardar el estado y los nuevos cambioEstado)
        # También incluye la modificación de los datos del evento (valor Magnitud, alcance y origen) (si es que estos fueron modificados)
        self.eventoSismicoSeleccionadoActual = repoEventoSismico.update(self.eventoSismicoSeleccionadoActual)


    def actualizarEstadoAConfirmado(self):
        self.getFechaHora()
        self.eventoSismicoSeleccionadoActual.confirmar(self.analistaLogueado, self.fechaHoraActual)
        print('-'*100)
        print("evento confirmado")
        print('-'*100)
        repoEventoSismico = EventoSismicoRepository()
        # Guardar los cambios realizados al evento sismico (incluye guardar el estado y los nuevos cambioEstado)
        self.eventoSismicoSeleccionadoActual = repoEventoSismico.update(self.eventoSismicoSeleccionadoActual)


    def finCasoDeUso(self): #TODO no se que debería hacer con esto, si es que debería hacer algo, cerrar la venta quizás(?
        print("Fin del caso de uso")
        self.punteroPantalla.volverApantallaPrincipal()
        print(self)


    @staticmethod
    def validarExistenciaMagnitudAlcanceOrigen(valorMagnitudMod, alcanceMod, origenGeneracionMod):
        if valorMagnitudMod is not None and alcanceMod is not None and origenGeneracionMod is not None:
            return True
        else:
            return False


    def casoDeUsoCancelado(self):
        print("Caso de uso cancelado")
        self.buscarUsuarioLogueado()
        self.getFechaHora()
        self.eventoSismicoSeleccionadoActual.actualizarEstadoPendiente(self.analistaLogueado, self.fechaHoraActual)
        print(self)




