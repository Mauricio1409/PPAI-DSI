from __future__ import annotations
from typing import Optional
from decimal import Decimal
from datetime import datetime
from sqlalchemy import Integer, Text, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.database.engine.base import Base

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from infrastructure.database.models.EventoSismicoORM import EventoSismicoORM
    from infrastructure.database.models.MuestraSismicaORM import MuestraSismicaORM
    from infrastructure.database.models.SismografoORM import SismografoORM

class SerieTemporalORM(Base):
    __tablename__ = "SERIE_TEMPORAL"

    serieTemporalId: Mapped[int] = mapped_column("SERIE_TEMPORAL_ID", Integer, primary_key=True, autoincrement=True)
    condicionAlarma: Mapped[Optional[str]] = mapped_column("CONDICION_ALARMA", Text)
    fechaHoraInicioRegistroMuestras: Mapped[Optional[datetime]] = mapped_column("FECHA_HORA_INICIO_REGISTRO_MUESTRAS", DateTime(timezone=False))
    fechaHoraRegistro: Mapped[Optional[datetime]] = mapped_column("FECHA_HORA_REGISTRO", DateTime(timezone=False))
    frecuenciaMuestreo: Mapped[Optional[Decimal]] = mapped_column("FRECUENCIA_MUESTREO", Numeric)

    sismografoId: Mapped[int] = mapped_column(
        "SISMOGRAFO_ID",
        ForeignKey("SISMOGRAFO.SISMOGRAFO_ID"),
        nullable=False
    )
    eventoSismicoId: Mapped[int] = mapped_column(
        "EVENTO_SISMICO_ID",
        ForeignKey("EVENTO_SISMICO.EVENTO_SISMICO_ID"),
        nullable=False
    )

    # Relaciones
    sismografo: Mapped["SismografoORM"] = relationship(
        back_populates="seriesTemporales",
        lazy="joined"
    )
    eventoSismico: Mapped["EventoSismicoORM"] = relationship(
        back_populates="seriesTemporales",
        lazy="joined"
    )
    muestras: Mapped[list["MuestraSismicaORM"]] = relationship(
        back_populates="serieTemporal",
        lazy="joined"
    )
