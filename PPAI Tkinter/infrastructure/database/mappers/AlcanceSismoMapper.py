from infrastructure.database.models.AlcanceSismoORM import AlcanceSismoORM
from Entitys.AlcanceSismo import AlcanceSismo

class AlcanceSismoMapper:
    @staticmethod
    def toDomain(alcanceSismoORM: AlcanceSismoORM):
        return AlcanceSismo(
            descripcion=alcanceSismoORM.descripcion,
            nombre=alcanceSismoORM.nombre
        )
    @staticmethod
    def toORM(alcanceSismo: AlcanceSismo):
        return AlcanceSismoORM(
            alcanceSismoId=alcanceSismo.alcanceSismoId,
            descripcion=alcanceSismo.descripcion,
            nombre=alcanceSismo.nombre
        )
    @staticmethod
    def newToORM(alcanceSismo: AlcanceSismo):
        return AlcanceSismoORM(
            descripcion=alcanceSismo.descripcion,
            nombre=alcanceSismo.nombre
        )