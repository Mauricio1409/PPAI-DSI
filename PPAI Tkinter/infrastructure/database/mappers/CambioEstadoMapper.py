from Entitys.CambioEstado import CambioEstado
from infrastructure.database.mappers.AnalistaSismoMapper import AnalistaSismoMapper
from infrastructure.database.mappers.EstadoMapper import EstadoMapper
from infrastructure.database.models.CambioEstadoORM import CambioEstadoORM


class CambioEstadoMapper:
    @staticmethod
    def toDomain(orm: CambioEstadoORM) -> CambioEstado:
        return CambioEstado(
            cambioEstadoId=orm.cambioEstadoId,
            fechaHoraFin=orm.fechaHoraFin,
            fechaHoraInicio=orm.fechaHoraInicio,
            estado=EstadoMapper.toDomain(orm.estado),
            analista=AnalistaSismoMapper.toDomain(orm.analista)
        )

    @staticmethod
    def toORM(entity: CambioEstado) -> CambioEstadoORM:
        return CambioEstadoORM(
            cambioEstadoId=entity.cambioEstadoId,
            fechaHoraFin=entity.fechaHoraFin,
            fechaHoraInicio=entity.fechaHoraInicio,
            estado=EstadoMapper.toORM(entity.estado),
            analista=AnalistaSismoMapper.toORM(entity.analistaResponsable)
        )

    @staticmethod
    def NewToORM(entity: CambioEstado) -> CambioEstadoORM:
        return CambioEstadoORM(
            fechaHoraFin=entity.fechaHoraFin,
            fechaHoraInicio=entity.fechaHoraInicio,
            estado=EstadoMapper.toORM(entity.estado),
            analista=AnalistaSismoMapper.toORM(entity.analistaResponsable)
        )
