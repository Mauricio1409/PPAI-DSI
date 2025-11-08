from datetime import datetime, timedelta

from Entitys.AlcanceSismo import AlcanceSismo
from Entitys.AnalistaSismos import AnalistaSismos
from Entitys.CambioEstado import CambioEstado
from Entitys.ClasificacionSismo import ClasificacionSismo
from Entitys.DetalleMuestraSismica import DetalleMuestraSismica
from Entitys.EstacionSismologica import EstacionSismologica
from Entitys.EventoSismico import EventoSismico
from Entitys.MagnitudRichter import MagnitudRichter
from Entitys.MuestraSismica import MuestraSismica
from Entitys.OrigenDeGeneracion import OrigenDeGeneracion
from Entitys.STATE.AutoDetectado import AutoDetectado
from Entitys.STATE.PendienteDeRevision import PendienteDeRevision
from Entitys.SerieTemporal import SerieTemporal
from Entitys.Sismografo import Sismografo
from Entitys.tipoDato import TipoDato
from infrastructure.database.repositories.EventoSismicoRepository import EventoSismicoRepository

repo = EventoSismicoRepository()

print(repo.get_all())

estado1=AutoDetectado()
estado2=PendienteDeRevision()

analistaSismo1=AnalistaSismos("Julian", "Alvarez")

cambioEstado1 = CambioEstado(datetime.now(), estado1, analistaSismo1, datetime.now())

cambioEstado2 = CambioEstado(datetime.now(), estado2, analistaSismo1, None)


tipoDato1 = TipoDato("test", "test_unit", 100)

detalle_muestra1 = DetalleMuestraSismica(112.3, tipoDato1)
detalle_muestra2 = DetalleMuestraSismica(112.5, tipoDato1)
detalle_muestra3 = DetalleMuestraSismica(113.5, tipoDato1)
detalle_muestra4 = DetalleMuestraSismica(129.2, tipoDato1)

muestraSismica1 = MuestraSismica(datetime.now(), [detalle_muestra1, detalle_muestra2])

muestraSismica2 = MuestraSismica(datetime.now(), [detalle_muestra3, detalle_muestra4])

serieTemporal1 = SerieTemporal("Alarma_test", datetime.now(), datetime.now() + timedelta(hours=1), 112.3,
                               [muestraSismica1, muestraSismica2], 
                               Sismografo(datetime.now() - timedelta(hours=1), 777, 
                                          EstacionSismologica(123, 12, datetime.now(),
                                                              11.2, 13.2, "testEstacion",14)))


obj1 = EventoSismico(datetime.now(), MagnitudRichter("test", 3), 11.3, 12.4,
                     [cambioEstado1, cambioEstado2], estado2,
                     ClasificacionSismo(11, 30, "test"),
                     11.3, 12.4, AlcanceSismo("test", "alcance_test"),
                     OrigenDeGeneracion("test", "origen_test"), [serieTemporal1], 11.3)

repo.save(obj1)

print("se creo un nuevo registro")

print("se actualizo el id del objeto dominio: ", obj1.eventoSismicoId)

print("se obtiene todos los registros")
print(repo.get_all())