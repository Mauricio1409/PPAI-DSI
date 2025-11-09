from infrastructure.database.models.SismografoORM import SismografoORM
from Entitys.Sismografo import Sismografo
from infrastructure.database.mappers.EstacionSismologicaMapper import EstacionSismologicaMapper


class SismografoMapper:
    @staticmethod
    def toDomain(orm: SismografoORM) -> Sismografo:
        estacion = EstacionSismologicaMapper.toDomain(orm.estacionSismologica) if orm.estacionSismologica else None
        return Sismografo(
            sismografoId=orm.sismografoId,
            fechaAdquisicion=orm.fechaAdquisicion,
            numeroSerie=orm.numeroSerie or 0,
            estacionSismologica=estacion,
        )

    @staticmethod
    def toORM(entity: Sismografo) -> SismografoORM:
        return SismografoORM(
            sismografoId=entity.sismografoId,
            fechaAdquisicion=entity.fechaAdquisicion,
            numeroSerie=entity.numeroSerie,
            estacionSismologica=EstacionSismologicaMapper.toORM(entity.estacionSismologica) if entity.estacionSismologica else None,
        )