from __future__ import annotations
from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.database.engine.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from infrastructure.database.models.SerieTemporalORM import SerieTemporalORM
    from infrastructure.database.models.DetalleMuestraSismicaORM import DetalleMuestraSismicaORM

class MuestraSismicaORM(Base):
    __tablename__ = "MUESTRA_SISMICA"

    muestraSismicaId: Mapped[int] = mapped_column("MUESTRA_SISMICA_ID", Integer, primary_key=True, autoincrement=True)
    fechaHoraMuestra: Mapped[Optional[datetime]] = mapped_column("FECHA_HORA_MUESTRA", DateTime(timezone=False))
    serieTemporalId: Mapped[int] = mapped_column(
        "SERIE_TEMPORAL_ID",
        ForeignKey("SERIE_TEMPORAL.SERIE_TEMPORAL_ID"),
        nullable=False
    )

    serieTemporal: Mapped["SerieTemporalORM"] = relationship(
        back_populates="muestras",
        lazy="joined"
    )
    detalles: Mapped[list["DetalleMuestraSismicaORM"]] = relationship(
        back_populates="muestraSismica",
        lazy="joined"
    )
