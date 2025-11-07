from infrastructure.database.models.SesionORM import SesionORM
from Entitys.Sesion import Sesion
from infrastructure.database.mappers.UsuarioMapper import UsuarioMapper


class SesionMapper:
    @staticmethod
    def toDomain(orm: SesionORM) -> Sesion:
        usuario_domain = UsuarioMapper.toDomain(orm.usuario) if orm.usuario else None
        return Sesion(
            sesion_id=orm.sesionId,
            usuario=usuario_domain,
            fechaHoraInicio=orm.fechaHoraInicio,
            fechaHoraFin=orm.fechaHoraFin,
        )

    @staticmethod
    def toORM(entity: Sesion) -> SesionORM:
        usuario=UsuarioMapper.toORM(entity.usuario) if entity.usuario else None
        return SesionORM(
            sesionId=entity.sesion_id,
            usuario=usuario,
            fechaHoraInicio=entity.fechaHoraInicio,
            fechaHoraFin=entity.fechaHoraFin,
        )

    @staticmethod
    def newToORM(entity: Sesion) -> SesionORM:
        usuario=UsuarioMapper.toORM(entity.usuario) if entity.usuario else None
        return SesionORM(
            fechaHoraInicio=entity.fechaHoraInicio,
            fechaHoraFin=entity.fechaHoraFin,
            usuario=usuario
        )
