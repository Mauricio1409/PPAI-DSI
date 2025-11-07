from Entitys.EventoSismico import EventoSismico
from infrastructure.database.mappers.AlcanceSismoMapper import AlcanceSismoMapper
from infrastructure.database.mappers.CambioEstadoMapper import CambioEstadoMapper
from infrastructure.database.mappers.ClasificacionSismoMapper import ClasificacionSismoMapper
from infrastructure.database.mappers.EstadoMapper import EstadoMapper
from infrastructure.database.mappers.MagnitudRichterMapper import MagnitudRichterMapper
from infrastructure.database.mappers.OrigenGeneracionMapper import OrigenGeneracionMapper
from infrastructure.database.mappers.SerieTemporalMapper import SerieTemporalMapper
from infrastructure.database.models.EventoSismicoORM import EventoSismicoORM


class EventoSismicoMapper:
    @staticmethod
    def toDomain(orm: EventoSismicoORM) -> EventoSismico:
        return EventoSismico(
            eventoSismicoId=orm.eventoSismicoId,
            fechaHoraOcurrencia=orm.fechaHoraOcurrencia,
            magnitud=MagnitudRichterMapper.toDomain(orm.magnitudRitcher),
            latitud_epicentro=float(orm.latitudEpicentro),
            longitud_epicentro=float(orm.longitudEpicentro),
            latitud_hipocentro=float(orm.latitudHipocentro),
            longitud_hipocentro=float(orm.longitudHipocentro),
            clasificacionSismo=ClasificacionSismoMapper.toDomain(orm.clasificacionSismo),
            alcanceSismo=AlcanceSismoMapper.toDomain(orm.alcanceSismo),
            origenGenercion=OrigenGeneracionMapper.toDomain(orm.origenGeneracion),
            seriesTemporales=[SerieTemporalMapper.toDomain(serie) for serie in orm.seriesTemporales],
            estado=EstadoMapper.toDomain(orm.estado),
            cambioEstado=[CambioEstadoMapper.toDomain(cambio) for cambio in orm.cambiosEstado]
        )