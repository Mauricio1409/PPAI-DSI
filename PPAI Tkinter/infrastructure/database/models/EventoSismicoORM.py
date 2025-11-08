from __future__ import annotations
from typing import Optional
from decimal import Decimal
from datetime import datetime

from sqlalchemy import Integer, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.database.engine.base import Base


from typing import TYPE_CHECKING

from infrastructure.database.models.EstadoOrm import EstadoORM

if TYPE_CHECKING:
    from infrastructure.database.models.SerieTemporalORM import SerieTemporalORM
    from infrastructure.database.models.ClasificacionSismoORM import ClasificacionSismoORM
    from infrastructure.database.models.MagnitudRitcher import MagnitudRitcherORM
    from infrastructure.database.models.AlcanceSismoORM import AlcanceSismoORM
    from infrastructure.database.models.OrigenGeneracionORM import OrigenGeneracionORM
    from infrastructure.database.models.CambioEstadoORM import CambioEstadoORM

class EventoSismicoORM(Base):
    __tablename__ = "EVENTO_SISMICO"

    eventoSismicoId: Mapped[int] = mapped_column("EVENTO_SISMICO_ID", Integer, primary_key=True, autoincrement=True)
    fechaHoraOcurrencia: Mapped[Optional[datetime]] = mapped_column("FECHA_HORA_OCURRENCIA", DateTime(timezone=False))
    latitudEpicentro: Mapped[Optional[Decimal]] = mapped_column("LATITUD_EPICENTRO", Numeric)
    latitudHipocentro: Mapped[Optional[Decimal]] = mapped_column("LATITUD_HIPOCENTRO", Numeric)
    longitudEpicentro: Mapped[Optional[Decimal]] = mapped_column("LONGITUD_EPICENTRO", Numeric)
    longitudHipocentro: Mapped[Optional[Decimal]] = mapped_column("LONGITUD_HIPOCENTRO", Numeric)
    valorMagnitud: Mapped[Optional[Decimal]] = mapped_column("VALOR_MAGNITUD", Numeric)

    clasificacionSismoId: Mapped[Optional[int]] = mapped_column(
        "CLASIFICACION_SISMO_ID",
        ForeignKey("CLASIFICACION_SISMO.CLASIFICACION_SISMO_ID"),
        nullable=True,
    )
    magnitudRitcherId: Mapped[Optional[int]] = mapped_column(
        "MAGNITUD_RITCHER_ID",
        ForeignKey("MAGINTUD_RITCHER.MAGNITUD_RITCHER_ID"),
        nullable=True,
    )
    alcanceSismoId: Mapped[Optional[int]] = mapped_column(
        "ALCANCE_SISMO_ID",
        ForeignKey("ALCANCE_SISMO.ALCANCE_SISMO_ID"),
        nullable=True,
    )
    origenGeneracionId: Mapped[Optional[int]] = mapped_column(
        "ORIGEN_GENERACION_ID",
        ForeignKey("ORIGEN_GENERACION.ORIGEN_GENERACION_ID"),
        nullable=True,
    )
    estadoId: Mapped[Optional[int]] = mapped_column(
        "ESTADO_ID",
        ForeignKey("ESTADO.ESTADO_ID"),
    )

    seriesTemporales: Mapped[list["SerieTemporalORM"]] = relationship(
        back_populates="eventoSismico",
        lazy="joined"
    )

    clasificacionSismo: Mapped[Optional["ClasificacionSismoORM"]] = relationship(lazy="joined")
    magnitudRitcher: Mapped[Optional["MagnitudRitcherORM"]] = relationship(lazy="joined")
    alcanceSismo: Mapped[Optional["AlcanceSismoORM"]] = relationship(lazy="joined")
    origenGeneracion: Mapped[Optional["OrigenGeneracionORM"]] = relationship(lazy="joined")
    estado: Mapped[Optional["EstadoORM"]] = relationship(lazy="joined")

    # Inversa de CAMBIO_ESTADO.eventoSismico
    cambiosEstado: Mapped[list["CambioEstadoORM"]] = relationship(
        lazy="joined"
    )

