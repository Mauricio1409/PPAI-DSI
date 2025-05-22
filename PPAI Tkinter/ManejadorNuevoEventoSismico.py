from datetime import datetime
from Entitys.EventoSismico import EventoSismico

from data import eventosSismicos, estados, sesion1

class ManejadorNuevoEventoSismico:

    def actualizarEventoABloqueado(self, eventoSismico: EventoSismico):
        for estado in self.arrayEstados :
            if estado.esAmbitoEvento():
                if estado.sosBloqueado():
                    self.estadoBloqueado = estado
        self.buscarUsuarioLogueado()
        self.getFechaHora()
        eventoSismico.revisar(self.estadoBloqueado, self.analistaLogueado, self.fechaHoraActual)

    def buscarUsuarioLogueado(self):
        self.analistaLogueado = self.sesion.obtenerUsuario()

    def getFechaHora(self):
        self.fechaHoraActual= datetime.now()

    def eventoSismicoSeleccionado(self, index):
        print(f"Se selecciono el evento sismico en el indice {index}, es el objeto {self.eventosPendienteRevision[index]}")
        self.eventoSismicoSeleccionadoActual = self.eventosPendienteRevision[index]
        self.actualizarEventoABloqueado(self.eventoSismicoSeleccionadoActual)
        self.buscarDatosevento(self.eventoSismicoSeleccionadoActual)
        self.clasificarPorEstacion()
        for clavedato, dato in self.datosEventoSismico.items(): #todo esto lo hice simplemente para ver que funcionase y recuperase los datos que se necesitan
            print(f"{clavedato}: {dato}")
        self.punteroPantalla.mostrarOpcionMapa()

    def buscarDatosevento(self, evento: EventoSismico):
        self.datosEventoSismico = evento.obtenerDatos()
        print(self.datosEventoSismico)


#TODO CHEQUEAR ESTO
    def clasificarPorEstacion(self):
        for i in range(len(self.datosEventoSismico["seriesTemporales"])):
            for j in range(i + 1, len(self.datosEventoSismico["seriesTemporales"])):
                if self.datosEventoSismico["seriesTemporales"][i]["estacionSismologica"]["codigoEstacion"] > self.datosEventoSismico["seriesTemporales"][j]["estacionSismologica"]["codigoEstacion"]:
                    # Intercambiar los elementos
                    self.datosEventoSismico["seriesTemporales"][i], self.datosEventoSismico["seriesTemporales"][j] = self.datosEventoSismico["seriesTemporales"][j], self.datosEventoSismico["seriesTemporales"][i]
                # Aquí puedes agregar lógica adicional para procesar las muestras



    def registrarNuevaRevision(self):
        self.buscar_eventos_auto_detectados()
        self.ordenarPorFechaHora()
        self.punteroPantalla.presentarEventosNoRevisados(self.arrayFechaHora, self.arrayUbicacion, self.arrayMagnitud)
        

    def ordenarPorFechaHora(self):
        for i in range(len(self.arrayFechaHora)):
            for j in range(i + 1, len(self.arrayFechaHora)):
                if self.arrayFechaHora[i] < self.arrayFechaHora[j]:
                    # Intercambiar los elementos
                    self.arrayFechaHora[i], self.arrayFechaHora[j] = self.arrayFechaHora[j], self.arrayFechaHora[i]
                    self.arrayUbicacion[i], self.arrayUbicacion[j] = self.arrayUbicacion[j], self.arrayUbicacion[i]
                    self.arrayMagnitud[i], self.arrayMagnitud[j] = self.arrayMagnitud[j], self.arrayMagnitud[i]
                    self.eventosPendienteRevision[i], self.eventosPendienteRevision[j] = self.eventosPendienteRevision[j], self.eventosPendienteRevision[i]

    def buscar_eventos_auto_detectados(self):
        for evento in self.eventosSismicos:
            
            if evento.esPendienteRevision():
                self.eventosPendienteRevision.append(evento)
                self.arrayFechaHora.append(evento.fechaHoraOcurrencia)
                self.arrayUbicacion.append(evento.getUbicacion())
                self.arrayMagnitud.append(evento.ValorMagnitud) ##CHEQUEAR ESTO CON EL DIAGRAMA

    def noVisualizarSeleccionado(self):
        self.punteroPantalla.habilitarEdicionDatos(self.datosEventoSismico["alcanceSismo"], self.datosEventoSismico["origenGeneracion"], self.eventoSismicoSeleccionadoActual.ValorMagnitud )



    def __init__(self,punteroPantalla):

        self.eventoSismicoSeleccionadoActual = None
        self.punteroPantalla = punteroPantalla
        self.eventosSismicos = eventosSismicos
        self.sesion = sesion1
        self.arrayEstados = estados

        self.eventosPendienteRevision = []
        self.arrayMagnitud = []
        self.arrayUbicacion = []
        self.arrayFechaHora = []

        self.eventoBloqueado = None
        self.fechaHoraActual = None
        self.analistaLogueado = None
        self.datosEventoSismico = None

