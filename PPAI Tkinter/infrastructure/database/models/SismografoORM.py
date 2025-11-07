from __future__ import annotations
from typing import Optional
from datetime import datetime
from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.database.engine.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from infrastructure.database.models.EstacionSismologicaORM import EstacionSismologicaORM
    from infrastructure.database.models.SerieTemporalORM import SerieTemporalORM

class SismografoORM(Base):
    __tablename__ = "SISMOGRAFO"

    sismografoId: Mapped[int] = mapped_column("SISMOGRAFO_ID", Integer, primary_key=True, autoincrement=True)
    fechaAdquisicion: Mapped[Optional[datetime]] = mapped_column("FECHA_ADQUISICION", DateTime(timezone=False))
    numeroSerie: Mapped[Optional[int]] = mapped_column("NUMERO_SERIE", Integer)

    estacionSismologicaId: Mapped[Optional[int]] = mapped_column(
        "ESTACION_SISMOLOGICA_ID",
        ForeignKey("ESTACION_SISMOLOGICA.ESTACION_SISMOLOGICA_ID"),
        nullable=True
    )

    # Relaciones
    estacionSismologica: Mapped[Optional["EstacionSismologicaORM"]] = relationship(
        back_populates="sismografos",
        lazy="joined"
    )
    # 1 → N con SerieTemporal (FK vive en SERIE_TEMPORAL)
    seriesTemporales: Mapped[list["SerieTemporalORM"]] = relationship(
        back_populates="sismografo",
        lazy="joined"
    )