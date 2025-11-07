from infrastructure.database.models.ClasificacionSismoORM import ClasificacionSismoORM
from Entitys.ClasificacionSismo import ClasificacionSismo


class ClasificacionSismoMapper:
    @staticmethod
    def toDomain(orm: ClasificacionSismoORM) -> ClasificacionSismo:
        return ClasificacionSismo(
            kmProfundidadDesde=orm.kmProfundidadDesde or 0,
            kmProfundidadHasta=orm.kmProfundidadHasta or 0,
            nombre=orm.nombre or "",
        )

    @staticmethod
    def toORM(entity: ClasificacionSismo) -> ClasificacionSismoORM:
        return ClasificacionSismoORM(
            clasificacionSismoId=entity.clasificacionSismoId,
            kmProfundidadDesde=entity.kmProfundidadDesde,
            kmProfundidadHasta=entity.kmProfundidadHasta,
            nombre=entity.nombre,
        )

    @staticmethod
    def newToORM(entity: ClasificacionSismo) -> ClasificacionSismoORM:
        return ClasificacionSismoORM(
            kmProfundidadDesde=entity.kmProfundidadDesde,
            kmProfundidadHasta=entity.kmProfundidadHasta,
            nombre=entity.nombre,
        )
