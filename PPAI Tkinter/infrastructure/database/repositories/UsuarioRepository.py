from Entitys.Usuario import Usuario
from infrastructure.database.mappers.UsuarioMapper import UsuarioMapper
from infrastructure.database.models.UsuarioORM import UsuarioORM
from infrastructure.database.unit_of_work.uow_factory import uow_factory


class UsuarioRepository:
    def __init__(self):
        self.uow_factory = uow_factory

    def get_all(self) -> list[Usuario]:
        with self.uow_factory() as uow:
            found = uow.session.query(UsuarioORM).all()
            return [UsuarioMapper.toDomain(item) for item in found]

    def get_by_id(self, userId: int) -> Usuario|None:
        with self.uow_factory() as uow:
            found = uow.session.query(UsuarioORM).filter(UsuarioORM.usuarioId == userId).first()
            return UsuarioMapper.toDomain(found) if found else None

    def save(self, entity: Usuario) -> None:
        with self.uow_factory() as uow:
            orm = UsuarioMapper.toORM(entity)
            uow.session.add(orm)
            uow.session.flush()
            entity.usuarioId = orm.usuarioId