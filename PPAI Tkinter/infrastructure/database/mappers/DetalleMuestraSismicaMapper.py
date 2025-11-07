from Entitys.DetalleMuestraSismica import DetalleMuestraSismica
from infrastructure.database.mappers.TipoDatoMapper import TipoDatoMapper
from infrastructure.database.models.DetalleMuestraSismicaORM import DetalleMuestraSismicaORM


class DetalleMuestraSismicaMapper:
    @staticmethod
    def toDomain(orm: DetalleMuestraSismicaORM) -> DetalleMuestraSismica:
        return DetalleMuestraSismica(
            detalleMuestraId=orm.detalleMuestraSismicaId,
            valor=float(orm.valor),
            tipo=TipoDatoMapper.toDomain(orm.tipoDato)
        )
    @staticmethod
    def toORM(entity: DetalleMuestraSismica) -> DetalleMuestraSismicaORM:
        return DetalleMuestraSismicaORM(
            detalleMuestraSismicaId=entity.detalleMuestraId,
            valor=entity.valor,
            tipoDato=TipoDatoMapper.toORM(entity.tipo)
        )
    @staticmethod
    def newToORM(entity: DetalleMuestraSismica) -> DetalleMuestraSismicaORM:
        return DetalleMuestraSismicaORM(
            valor=entity.valor,
            tipoDato=TipoDatoMapper.toORM(entity.tipo)
        )