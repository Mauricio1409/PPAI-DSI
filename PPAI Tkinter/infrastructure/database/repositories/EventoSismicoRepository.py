from Entitys.EventoSismico import EventoSismico
from infrastructure.database.mappers.EventoSismicoMapper import EventoSismicoMapper
from infrastructure.database.models.EventoSismicoORM import EventoSismicoORM
from infrastructure.database.unit_of_work.uow_factory import uow_factory



class EventoSismicoRepository:
    def __init__(self):
        self.uow_factory = uow_factory

    def get_all(self) -> list[EventoSismico]:
        with self.uow_factory() as uow:
            eventos = uow.session.query(EventoSismicoORM)
            return [EventoSismicoMapper.toDomain(evento) for evento in eventos]

    def save(self, eventoSismico: EventoSismico) -> None:
        with self.uow_factory() as uow:
            orm = EventoSismicoMapper.toORM(eventoSismico)
            uow.session.add(orm)
            uow.session.flush()
            eventoSismico.eventoSismicoId = orm.eventoSismicoId