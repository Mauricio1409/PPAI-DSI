from infrastructure.database.models.TipoDatoORM import TipoDatoORM
from Entitys.tipoDato import TipoDato


class TipoDatoMapper:
    @staticmethod
    def toDomain(orm: TipoDatoORM) -> TipoDato:
        return TipoDato(
            tipoDatoId=orm.tipoDatoId,
            denominacion=orm.denominacion,
            nombreUnidadMedida=orm.unidadMedida,
            valorUmbral=float(orm.valorUmbral),
        )

    @staticmethod
    def toORM(entity: TipoDato) -> TipoDatoORM:
        return TipoDatoORM(
            tipoDatoId=entity.tipoDatoId,
            denominacion=entity.denominacion,
            unidadMedida=entity.nombreUnidadMedida,
            valorUmbral=entity.valorUmbral,
        )

