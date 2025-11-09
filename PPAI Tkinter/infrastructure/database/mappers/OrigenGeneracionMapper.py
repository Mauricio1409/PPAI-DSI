from infrastructure.database.models.OrigenGeneracionORM import OrigenGeneracionORM
from Entitys.OrigenDeGeneracion import OrigenDeGeneracion


class OrigenGeneracionMapper:
    @staticmethod
    def toDomain(orm: OrigenGeneracionORM) -> OrigenDeGeneracion:
        return OrigenDeGeneracion(
            origenDeGeneracionId=orm.origenGeneracionId,
            descripcion=orm.descripcion,
            nombre=orm.nombre,
        )

    @staticmethod
    def toORM(entity: OrigenDeGeneracion) -> OrigenGeneracionORM:
        return OrigenGeneracionORM(
            origenGeneracionId=entity.origenDeGeneracionId,
            descripcion=entity.descripcion,
            nombre=entity.nombre,
        )
