from infrastructure.database.models.UsuarioORM import UsuarioORM
from Entitys.Usuario import Usuario
from infrastructure.database.mappers.AnalistaSismoMapper import AnalistaSismoMapper


class UsuarioMapper:
    @staticmethod
    def toDomain(orm: UsuarioORM) -> Usuario:
        analista_domain = AnalistaSismoMapper.toDomain(orm.analista) if orm.analista else None
        return Usuario(
            usuarioId=orm.usuarioId,
            nombre=orm.nombre,
            contrasena=orm.contrasena,
            logueado=analista_domain,
        )

    @staticmethod
    def toORM(entity: Usuario) -> UsuarioORM:
        return UsuarioORM(
            usuarioId=entity.usuarioId,
            nombre=entity.nombre,
            contrasena=entity.contrasena,
            analista=AnalistaSismoMapper.toORM(entity.logueado) if entity.logueado else None,
        )
