from infrastructure.database.models.EstacionSismologicaORM import EstacionSismologicaORM
from Entitys.EstacionSismologica import EstacionSismologica


class EstacionSismologicaMapper:
    @staticmethod
    def toDomain(orm: EstacionSismologicaORM) -> EstacionSismologica:
        return EstacionSismologica(
            estacionSismologicaId=orm.estacionSismologicaId,
            codigoEstacion=orm.codigoEstacion,
            documentoCertificacionAdq=orm.documentoCertificacionAdquisicion,
            fechaSolicitudCertificacion=orm.fechaSolicitudCertificacion,
            latitud=float(orm.latitud),
            longitud=float(orm.longitud),
            nombre=orm.nombre,
            numeroCertificacionAdquisicion=orm.numeroCertificacionAdquisicion,
        )

    @staticmethod
    def toORM(entity: EstacionSismologica) -> EstacionSismologicaORM:
        return EstacionSismologicaORM(
            estacionSismologicaId=entity.estacionSismologicaId,
            codigoEstacion=entity.codigoEstacion,
            documentoCertificacionAdquisicion=entity.documentoCertificacionAdq,
            fechaSolicitudCertificacion=entity.fechaSolicitudCertificacion,
            latitud=entity.latitud,
            longitud=entity.longitud,
            nombre=entity.nombre,
            numeroCertificacionAdquisicion=entity.numeroCertificacionAdquisicion,
        )
