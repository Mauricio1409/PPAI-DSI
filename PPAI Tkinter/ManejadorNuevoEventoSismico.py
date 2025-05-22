from datetime import datetime

from data import eventosSismicos, estados

class ManejadorNuevoEventoSismico:

# todo terminar de implementar la logica en la clase evento
    def actualizarEventoABloqueado(self, eventoSismico):
        for evento in eventosSismicos :
            if evento.esAmbitoEvento():
                if evento.sosBloqueado():
                    self.eventoBloqueado = evento

    def eventoSismicoSeleccionado(self, index):
        print(f"Se selecciono el evento sismico en el indice {index}, es el objeto {self.eventosPendienteRevision[index]}")


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


    def __init__(self,punteroPantalla):
        self.arrayMagnitud = []
        self.arrayUbicacion = []
        self.arrayFechaHora = []
        self.punteroPantalla = punteroPantalla
        self.eventosSismicos = eventosSismicos
        self.eventosPendienteRevision = []

