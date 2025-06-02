from datetime import datetime
from Entitys.EventoSismico import EventoSismico
from ManejadorGenerarSismograma import ManejadorGenerarSismograma

from data import eventosSismicos, estados, sesion1

class ManejadorNuevoEventoSismico:

    def __init__(self,punteroPantalla):

        self.punteroPantalla = punteroPantalla
        self.eventosSismicos = eventosSismicos
        self.sesion = sesion1
        self.arrayEstados = estados

        self.eventosPendienteRevision = []
        self.arrayDatos = []
        # self.arrayMagnitud = []
        # self.arrayUbicacion = []
        # self.arrayFechaHora = []

        self.estadoConfirmado = None
        self.CasoUsoSismograma = None
        self.datosModificados = False
        self.ValorMagnitudMod = None
        self.origenGeneracionMod = None
        self.alcanceMod = None
        self.datosSerieTemporal = None
        self.estadoBloqueado = None
        self.eventoSismicoSeleccionadoActual = None
        self.estadoRechazado = None
        self.eventoBloqueado = None
        self.fechaHoraActual = None
        self.analistaLogueado = None
        self.datosEventoSismico = None

    def registrarNuevaRevision(self):
        self.buscarEventosAutoDetectados()
        self.ordenarPorFechaHora()
        self.punteroPantalla.presentarEventosNoRevisados(self.arrayDatos)

    def buscarEventosAutoDetectados(self):
        self.arrayDatos = []
        for evento in self.eventosSismicos:
            datos_evento = {}
            if evento.esPendienteRevision():
                # self.eventosPendienteRevision.append(evento)
                # self.arrayFechaHora.append(evento.fechaHoraOcurrencia)
                # self.arrayUbicacion.append(evento.getUbicacion())
                # self.arrayMagnitud.append(evento.ValorMagnitud) ##CHEQUEAR ESTO CON EL DIAGRAMA
                datos_evento['evento'] = evento
                datos_evento['fechaHoraOcurrencia'] = evento.fechaHoraOcurrencia
                datos_evento['ubicacion'] = evento.getUbicacion()
                datos_evento['valorMagnitud'] = evento.ValorMagnitud

                self.arrayDatos.append(datos_evento)

    def ordenarPorFechaHora(self):

            self.arrayDatos.sort(key= lambda datosEvento : datosEvento['fechaHoraOcurrencia'], reverse=True)
            
            # for i in range(len(self.arrayFechaHora)):
            #     for j in range(i + 1, len(self.arrayFechaHora)):
            #         if self.arrayFechaHora[i] < self.arrayFechaHora[j]:
            #             # Intercambiar los elementos
            #             self.arrayFechaHora[i], self.arrayFechaHora[j] = self.arrayFechaHora[j], self.arrayFechaHora[i]
            #             self.arrayUbicacion[i], self.arrayUbicacion[j] = self.arrayUbicacion[j], self.arrayUbicacion[i]
            #             self.arrayMagnitud[i], self.arrayMagnitud[j] = self.arrayMagnitud[j], self.arrayMagnitud[i]
            #             self.eventosPendienteRevision[i], self.eventosPendienteRevision[j] = self.eventosPendienteRevision[j], self.eventosPendienteRevision[i]

    def eventoSismicoSeleccionado(self, index):
        print(f"Se selecciono el evento sismico en el indice {index}, es el objeto {self.arrayDatos[index]['evento']}")
        self.eventoSismicoSeleccionadoActual = self.arrayDatos[index]['evento']
        self.actualizarEventoABloqueado(self.eventoSismicoSeleccionadoActual)
        self.buscarDatosEvento(self.eventoSismicoSeleccionadoActual)
        self.clasificarPorEstacion()
        for clavedato, dato in self.datosEventoSismico.items(): #todo esto lo hice simplemente para ver que funcionase y recuperase los datos que se necesitan
            print(f"{clavedato}: {dato}")
        ruta_sismo =  self.generarSismograma(self.datosSerieTemporal)
        self.punteroPantalla.mostrarDetallesEvento(self.datosEventoSismico["clasificacionSismo"], ruta_sismo)
        self.punteroPantalla.mostrarOpcionMapa()

    def actualizarEventoABloqueado(self, eventoSismico: EventoSismico):
        for estado in self.arrayEstados :
            if estado.esAmbito('EventoSismico'):
                if estado.sosBloqueado():
                    self.estadoBloqueado = estado
        self.buscarUsuarioLogueado()
        self.getFechaHora()
        eventoSismico.revisar(self.estadoBloqueado, self.analistaLogueado, self.fechaHoraActual)

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
        
        #for i in range(len(self.datosEventoSismico["seriesTemporales"])):
        #    for j in range(i + 1, len(self.datosEventoSismico["seriesTemporales"])):
        #        if self.datosEventoSismico["seriesTemporales"][i]["estacionSismologica"]["codigoEstacion"] > self.datosEventoSismico["seriesTemporales"][j]["estacionSismologica"]["codigoEstacion"]:
                    # Intercambiar los elementos
        #            self.datosEventoSismico["seriesTemporales"][i], self.datosEventoSismico["seriesTemporales"][j] = self.datosEventoSismico["seriesTemporales"][j], self.datosEventoSismico["seriesTemporales"][i]
                # Aquí puedes agregar lógica adicional para procesar las muestras

    def generarSismograma(self, datosSerieTemporal): # TODO: Implementar lógica para generar sismograma
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
                self.eventoSismicoSeleccionadoActual.ValorMagnitud = valorMagnitud
                self.eventoSismicoSeleccionadoActual.alcanceSismo.nombre = alcanceSismo
                self.eventoSismicoSeleccionadoActual.origenGeneracion.nombre = origenGeneracion
                print("Datos modificados correctamente")

            if opcion == "Confirmar Evento":
                for estado in estados:
                    if estado.esAmbito("EventoSismico"):
                        if estado.sosConfirmado():
                            self.estadoConfirmado = estado
                self.getFechaHora()
                self.eventoSismicoSeleccionadoActual.actualizarEstadoConfirmado(self.estadoConfirmado, self.analistaLogueado, self.fechaHoraActual)
                print("evento confirmado")
                self.finCasoDeUso()

            elif opcion == "Rechazar Evento":

                self.getFechaHora()
                for estado in estados:
                    if estado.esAmbito("EventoSismico"):
                        if estado.sosRechazado():
                            self.estadoRechazado = estado

                self.eventoSismicoSeleccionadoActual.actualizarEstadoRechazado(self.estadoRechazado, self.analistaLogueado, self.fechaHoraActual)
                self.finCasoDeUso()

            elif opcion == "Solicitar Revisión a Experto":
                # TODO Lógica para solicitar revisión
                print("Revision Solicitada")
        else:
            print("No se tienen los datos necesarios del evento sismico.")


    def validarExistenciaMagnitudAlcanceOrigen(self, valorMagnitudMod, alcanceMod, origenGeneracionMod):
        if valorMagnitudMod is not None and alcanceMod is not None and origenGeneracionMod is not None:
            return True
        else:
            return False

    def finCasoDeUso(self): #TODO no se que debería hacer con esto, si es que debería hacer algo, cerrar la venta quizás(?
        print("Fin del caso de uso")
        self.punteroPantalla.volverApantallaPrincipal()
        print(self)


    def casoDeUsoCancelado(self):
        print("Caso de uso cancelado")
        estado_pendiente_revision = self.buscarEstadoPendienteRevision()

        self.buscarUsuarioLogueado()

        self.getFechaHora()

        self.eventoSismicoSeleccionadoActual.actualizarEstadoPendiente(estado_pendiente_revision, self.analistaLogueado, self.fechaHoraActual)
        print(self)


    def buscarEstadoPendienteRevision(self):
        for estado in self.arrayEstados:
            if estado.esAmbito('EventoSismico'):
                if estado.sosPendienteRevision():
                    return estado
        return None

