from __future__ import annotations
from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.database.engine.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from infrastructure.database.models.EstadoOrm import EstadoORM
    from infrastructure.database.models.AnalistaSismosORM import AnalistaSismosORM


class CambioEstadoORM(Base):
    __tablename__ = "CAMBIO_ESTADO"

    cambioEstadoId: Mapped[int] = mapped_column("CAMBIO_ESTADO_ID", Integer, primary_key=True, autoincrement=True)
    fechaHoraInicio: Mapped[Optional[datetime]] = mapped_column("FECHA_HORA_INICIO", DateTime(timezone=False))
    fechaHoraFin: Mapped[Optional[datetime]] = mapped_column("FECHA_HORA_FIN", DateTime(timezone=False))
    eventoSismicoId: Mapped[int] = mapped_column(
        "EVENTO_SISMICO_ID",
        ForeignKey("EVENTO_SISMICO.EVENTO_SISMICO_ID"),
        nullable=False
    )
    estadoId: Mapped[int] = mapped_column(
        "ESTADO_ID",
        ForeignKey("ESTADO.ESTADO_ID"),
        nullable=False
    )
    analistaId: Mapped[int] = mapped_column(
        "ANALISTA_ID",
        ForeignKey("ANALISTA_SISMOS.ANALISTA_ID"),
        nullable=False
    )

    # Back-pop hacia EventoSismicoORM.cambiosEstado
    estado: Mapped["EstadoORM"] = relationship(lazy="joined")
    analista: Mapped["AnalistaSismosORM"] = relationship(lazy="joined")


    def __repr__(self):
        return f"<CambioEstadoORM(cambioEstadoId={self.cambioEstadoId}, fechaHoraInicio={self.fechaHoraInicio}, fechaHoraFin={self.fechaHoraFin}, eventoSismicoId={self.eventoSismicoId}, estadoId={self.estadoId}, analistaId={self.analistaId})>"