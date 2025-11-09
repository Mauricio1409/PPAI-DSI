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
            valorMagnitud=float(orm.valorMagnitud),
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

    @staticmethod
    def toORM(entity: EventoSismico) -> EventoSismicoORM:
        cambios_estado = []

        for cambio in entity.cambioEstado:
            cambioORM = CambioEstadoMapper.toORM(cambio)
            cambioORM.eventoSismicoId = entity.eventoSismicoId
            cambios_estado.append(cambioORM)

        print("-"*50)
        print('\n'*4)
        print("cambios_estado: ")
        for cambio in cambios_estado:
            print(cambio)
        print('\n' * 4)
        print("-"*50)

        return EventoSismicoORM(
            eventoSismicoId=entity.eventoSismicoId,
            fechaHoraOcurrencia=entity.fechaHoraOcurrencia,
            magnitudRitcher=MagnitudRichterMapper.toORM(entity.magnitud),
            valorMagnitud=entity.valorMagnitud,
            latitudEpicentro=entity.latitudEpicentro,
            longitudEpicentro=entity.longitudEpicentro,
            latitudHipocentro=entity.latitudHipocentro,
            longitudHipocentro=entity.longitudHipocentro,
            clasificacionSismo=ClasificacionSismoMapper.toORM(entity.clasificacionSismo),
            alcanceSismo=AlcanceSismoMapper.toORM(entity.alcanceSismo),
            origenGeneracion=OrigenGeneracionMapper.toORM(entity.origenGeneracion),
            seriesTemporales=[SerieTemporalMapper.toORM(serie) for serie in entity.seriesTemporales],
            estado=EstadoMapper.toORM(entity.estado),
            cambiosEstado=cambios_estado
        )