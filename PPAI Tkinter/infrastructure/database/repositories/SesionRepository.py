from Entitys.Sesion import Sesion
from infrastructure.database.mappers.SesionMapper import SesionMapper
from infrastructure.database.models.SesionORM import SesionORM
from infrastructure.database.unit_of_work.uow_factory import uow_factory


class SesionRepository:
    def __init__(self):
        self.uow_factory = uow_factory

    def get_all(self) -> list[Sesion]:
        with self.uow_factory() as uow:
            found = uow.session.query(SesionORM).all()
            return [SesionMapper.toDomain(item) for item in found]

    def save(self, entity: Sesion) -> None:
        with self.uow_factory() as uow:
            orm = SesionMapper.toORM(entity)
            uow.session.add(orm)
            uow.session.flush()
            entity.sesionId = orm.sesionId
