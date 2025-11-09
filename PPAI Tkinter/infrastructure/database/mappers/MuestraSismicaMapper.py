from Entitys.MuestraSismica import MuestraSismica
from infrastructure.database.mappers.DetalleMuestraSismicaMapper import DetalleMuestraSismicaMapper
from infrastructure.database.models.MuestraSismicaORM import MuestraSismicaORM


class MuestraSismicaMapper:
     @staticmethod
     def toDomain(orm: MuestraSismicaORM) -> MuestraSismica:
            return MuestraSismica(
                muestraSismicaId=orm.muestraSismicaId,
                fechaHoraMuestra=orm.fechaHoraMuestra,
                detalleMuestra=[DetalleMuestraSismicaMapper.toDomain(detalle) for detalle in orm.detalles]
            )
     @staticmethod
     def toORM(entity: MuestraSismica) -> MuestraSismicaORM:
            return MuestraSismicaORM(
                muestraSismicaId=entity.muestraSismicaId,
                fechaHoraMuestra=entity.fechaHoraMuestra,
                detalles=[DetalleMuestraSismicaMapper.toORM(detalle) for detalle in entity.detalles]
            )