from Entitys.SerieTemporal import SerieTemporal
from infrastructure.database.mappers.MuestraSismicaMapper import MuestraSismicaMapper
from infrastructure.database.mappers.SismografoMapper import SismografoMapper
from infrastructure.database.models.SerieTemporalORM import SerieTemporalORM


class SerieTemporalMapper:
     @staticmethod
     def toDomain(orm: SerieTemporalORM) -> SerieTemporal:
         return SerieTemporal(
             serieTemporalId=orm.serieTemporalId,
             condicionAlarma=orm.condicionAlarma,
             fechaHoraRegistro=orm.fechaHoraRegistro,
             fechaHoraInicioRegistroMuestras=orm.fechaHoraInicioRegistroMuestras,
             frecuenciaMuestreo=float(orm.frecuenciaMuestreo),
             sismografo=SismografoMapper.toDomain(orm.sismografo),
             muestraSismica=[MuestraSismicaMapper.toDomain(muestra) for muestra in orm.muestras]
         )

     @staticmethod
     def toORM(entity: SerieTemporal) -> SerieTemporalORM:
         return SerieTemporalORM(
             serieTemporalId=entity.serieTemporalId,
             condicionAlarma=entity.condicionAlarma,
             fechaHoraRegistro=entity.fechaHoraRegistro,
             fechaHoraInicioRegistroMuestras=entity.fechaHoraInicioRegistroMuestras,
             frecuenciaMuestreo=entity.frecuenciaMuestreo,
             sismografo=SismografoMapper.toORM(entity.sismografo),
             muestras=[MuestraSismicaMapper.toORM(muestra) for muestra in entity.muestras]
         )

     @staticmethod
     def newToORM(entity: SerieTemporal) -> SerieTemporalORM:
         return SerieTemporalORM(
             condicionAlarma=entity.condicionAlarma,
             fechaHoraRegistro=entity.fechaHoraRegistro,
             fechaHoraInicioRegistroMuestras=entity.fechaHoraInicioRegistroMuestras,
             frecuenciaMuestreo=entity.frecuenciaMuestreo,
             sismografo=SismografoMapper.toORM(entity.sismografo),
             muestras=[MuestraSismicaMapper.toORM(muestra) for muestra in entity.muestras]
         )