from infrastructure.database.models.AnalistaSismosORM import AnalistaSismosORM
from Entitys.AnalistaSismos import AnalistaSismos


class AnalistaSismoMapper:
    @staticmethod
    def toDomain(orm: AnalistaSismosORM) -> AnalistaSismos:
        return AnalistaSismos(
            nombre=orm.nombre,
            apellido=orm.apellido,
            analista_id=orm.analistaId,
        )

    @staticmethod
    def toORM(entity: AnalistaSismos) -> AnalistaSismosORM:
        return AnalistaSismosORM(
            analistaId=entity.id_analista,
            nombre=entity.nombre,
            apellido=entity.apellido,
        )

    @staticmethod
    def newToORM(entity: AnalistaSismos) -> AnalistaSismosORM:
        return AnalistaSismosORM(
            nombre=entity.nombre,
            apellido=entity.apellido,
        )
