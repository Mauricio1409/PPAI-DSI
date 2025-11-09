from infrastructure.database.models.MagnitudRitcher import MagnitudRitcherORM
from Entitys.MagnitudRichter import MagnitudRichter


class MagnitudRichterMapper:
    @staticmethod
    def toDomain(orm: MagnitudRitcherORM) -> MagnitudRichter:
        return MagnitudRichter(
            magnitudRichterId=orm.magnitudRitcherId,
            descripcionMagnitud=orm.descripcionMagnitud,
            numero=orm.numero,
        )

    @staticmethod
    def toORM(entity: MagnitudRichter) -> MagnitudRitcherORM:
        return MagnitudRitcherORM(
            magnitudRitcherId=entity.magnitudRichterId,
            descripcionMagnitud=entity.descripcionMagnitud,
            numero=entity.numero,
        )
