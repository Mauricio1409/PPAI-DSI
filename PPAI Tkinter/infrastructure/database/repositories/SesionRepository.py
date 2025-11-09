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
            orm = uow.session.merge(orm)
            uow.session.flush()
            entity.sesionId = orm.sesionId

    def update(self, sesion: Sesion) -> Sesion:
        id_sesion = sesion.sesion_id
        with self.uow_factory() as uow:
            orm = SesionMapper.toORM(sesion)
            uow.session.merge(orm)
            uow.session.flush()

            newSesionORM = uow.session.query(SesionORM).filter_by(sesionId=id_sesion).first()
            return SesionMapper.toDomain(newSesionORM)

    def get_actual(self) -> Sesion:
        with self.uow_factory() as uow:
            found = uow.session.query(SesionORM).filter(SesionORM.fechaHoraFin == None).first()
            return SesionMapper.toDomain(found) if found else None
