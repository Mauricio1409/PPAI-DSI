from Entitys.EventoSismico import EventoSismico
from Entitys.Estado import Estado
from datetime import datetime

class ManejadorNuevoEventoSismico:
    def registrarNuevaRevision(self):
        self.buscar_eventos_auto_detectados()
        self.ordenarPorFechaHora()
        self.punteroPantalla.presentarEventosNoRevisados(self.arrayFechaHora, self.arrayUbicacion, self.arrayMagnitud)
        

    def ordenarPorFechaHora(self):
        print("Ordenando eventos por fecha y hora...")
        for i in range(len(self.arrayFechaHora)):
            for j in range(i + 1, len(self.arrayFechaHora)):
                if self.arrayFechaHora[i] > self.arrayFechaHora[j]:
                    # Intercambiar los elementos
                    self.arrayFechaHora[i], self.arrayFechaHora[j] = self.arrayFechaHora[j], self.arrayFechaHora[i]
                    self.arrayUbicacion[i], self.arrayUbicacion[j] = self.arrayUbicacion[j], self.arrayUbicacion[i]
                    self.arrayMagnitud[i], self.arrayMagnitud[j] = self.arrayMagnitud[j], self.arrayMagnitud[i]

# voy a dejar datos harcodeados en el archivo data.py, asi despues del manejador usamos eso y tenemos todos los datos ahì #dale
    def buscar_eventos_auto_detectados(self):
        for evento in self.eventosSismicos:
            
            if evento.esPendienteRevision():
                print("gatito")
                self.eventosPendienteRevision.append(evento)
                self.arrayFechaHora.append(evento.fechaHoraOcurrencia)
                self.arrayUbicacion.append(evento.getUbicacion())
                self.arrayMagnitud.append(evento.ValorMagnitud) ##CHEQUEAR ESTO CON EL DIAGRAMA


    def __init__(self,punteroPantalla):
        self.arrayMagnitud = []
        self.arrayUbicacion = []
        self.arrayFechaHora = []
        self.punteroPantalla = punteroPantalla
        self.eventosSismicos = [
            EventoSismico(datetime(2023, 5, 21, 12, 0, 0), 5.0, -34.0, -58.0, None, Estado("PendienteRevision","EventoSismico"), None, None, None, None),
            EventoSismico(datetime(2023, 10, 2, 14, 30, 0), 4.5, -35.0, -59.0, None, Estado("PendienteRevision","EventoSismico"), None, None, None, None),
            EventoSismico(datetime(2025, 10, 1, 10, 0, 0), 5.5, -34.5, -58.5, None, Estado("PendienteRevision","EventoSismico"), None, None, None, None),
            EventoSismico(datetime(2023, 10, 3, 16, 0, 0), 6.0, -36.0, -60.0, None, Estado("PendienteRevision","EventoSismico"), None, None, None, None),
            EventoSismico(datetime(2023, 10, 4, 18, 0, 0), 7.0, -37.0, -61.0, None, Estado("PendienteRevision","EventoSismico"), None, None, None, None),
            EventoSismico(datetime(2023, 10, 5, 20, 0, 0), 5.7, -38.0, -62.0, None, Estado("PendienteRevision","EventoSismico"), None, None, None, None),
        ]
        self.eventosPendienteRevision = []

