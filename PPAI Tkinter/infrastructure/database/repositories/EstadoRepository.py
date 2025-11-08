from Entitys.STATE.Estado import Estado
from infrastructure.database.mappers.EstadoMapper import EstadoMapper
from infrastructure.database.models.EstadoOrm import EstadoORM
from infrastructure.database.unit_of_work.uow_factory import uow_factory


class EstadoRepository:
    def __init__(self):
        self.uow_factory = uow_factory

    def get_all(self) -> list[Estado]:
        with self.uow_factory() as uow:
            found = uow.session.query(EstadoORM).all()
            return [EstadoMapper.toDomain(item) for item in found]

