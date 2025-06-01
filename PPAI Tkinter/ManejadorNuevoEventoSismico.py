from datetime import datetime
from Entitys.EventoSismico import EventoSismico

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
            datosEvento = {}
            if evento.esPendienteRevision():
                # self.eventosPendienteRevision.append(evento)
                # self.arrayFechaHora.append(evento.fechaHoraOcurrencia)
                # self.arrayUbicacion.append(evento.getUbicacion())
                # self.arrayMagnitud.append(evento.ValorMagnitud) ##CHEQUEAR ESTO CON EL DIAGRAMA
                datosEvento['evento'] = evento
                datosEvento['fechaHoraOcurrencia'] = evento.fechaHoraOcurrencia
                datosEvento['ubicacion'] = evento.getUbicacion()
                datosEvento['valorMagnitud'] = evento.ValorMagnitud

                self.arrayDatos.append(datosEvento)

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

    def generarSismograma(self, estacionSismologica): # TODO: Implementar lógica para generar sismograma
        pass

    def noVisualizarSeleccionado(self):
        self.punteroPantalla.habilitarEdicionDatos(self.eventoSismicoSeleccionadoActual.alcanceSismo, 
                                                   self.eventoSismicoSeleccionadoActual.origenGeneracion.obtenerDatos(), 
                                                   self.eventoSismicoSeleccionadoActual.ValorMagnitud )
        self.punteroPantalla.habilitarSelectorOpciones()

    def tomarModificarDatos(self, alcanceSismo, origenGeneracion, valorMagnitud):
        self.eventoSismicoSeleccionadoActual.alcanceSismo = alcanceSismo
        self.eventoSismicoSeleccionadoActual.origenGeneracion = origenGeneracion
        self.eventoSismicoSeleccionadoActual.ValorMagnitud = valorMagnitud
        print(f"Alcance Sismo: {self.eventoSismicoSeleccionadoActual.alcanceSismo}, Origen Generación: {self.eventoSismicoSeleccionadoActual.origenGeneracion}, Magnitud: {self.eventoSismicoSeleccionadoActual.ValorMagnitud}")
        self.punteroPantalla.habilitarBotonConfirmar()     

    def tomarOptGrilla(self, opcion):
        if opcion == "Confirmar Evento":
        # TODO Lógica para confirmar evento
            print("evento confirmado")

        elif opcion == "Rechazar Evento":
            if self.validarExistenciaMagnitudAlcanceOrigen():
                pass
            else:
                print("No se puede rechazar el evento sismico, falta información")

            for estado in estados:
                if estado.esAmbito("EventoSismico"):
                    if estado.sosRechazado():
                        self.estadoRechazado = estado
            self.getFechaHora()
            self.eventoSismicoSeleccionadoActual.actualizarEstadoRechazado(self.estadoRechazado, self.analistaLogueado, self.fechaHoraActual)
            self.finCasoDeUso()

        elif opcion == "Solicitar Revisión a Experto":
            # TODO Lógica para solicitar revisión
            print("Revision Solicitada")

    #TODO CORREGIR ESTO
    def validarExistenciaMagnitudAlcanceOrigen(self):
        valor_magnitud=self.eventoSismicoSeleccionadoActual.ValorMagnitud
        valor_alcance=self.eventoSismicoSeleccionadoActual.alcanceSismo
        valor_origen=self.eventoSismicoSeleccionadoActual.origenGeneracion
        if valor_magnitud is not None and valor_alcance is not None and valor_origen is not None:
            return True
        else:
            return False

    def finCasoDeUso(self): #TODO no se que debería hacer con esto, si es que debería hacer algo, cerrar la venta quizás(?
        print("Fin del caso de uso")
        self.punteroPantalla.volverApantallaPrincipal()
        print(self)


