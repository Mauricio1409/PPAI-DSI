from __future__ import annotations
from typing import Optional
from decimal import Decimal
from datetime import datetime
from sqlalchemy import Integer, Numeric, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.database.engine.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from infrastructure.database.models.SismografoORM import SismografoORM

class EstacionSismologicaORM(Base):
    __tablename__ = "ESTACION_SISMOLOGICA"

    estacionSismologicaId: Mapped[int] = mapped_column("ESTACION_SISMOLOGICA_ID", Integer, primary_key=True)
    codigoEstacion: Mapped[Optional[int]] = mapped_column("CODIGO_ESTACION", Integer)
    documentoCertificacionAdquisicion: Mapped[Optional[int]] = mapped_column("DOCUMENTO_CERTIFICACION_ADQUISICION", Integer)
    fechaSolicitudCertificacion: Mapped[Optional[datetime]] = mapped_column("FECHA_SOLICITUD_CERTIFICACION", DateTime(timezone=False))
    latitud: Mapped[Optional[Decimal]] = mapped_column("LATITUD", Numeric)
    longitud: Mapped[Optional[Decimal]] = mapped_column("LONGITUD", Numeric)
    nombre: Mapped[Optional[str]] = mapped_column("NOMBRE", Text)
    numeroCertificacionAdquisicion: Mapped[Optional[int]] = mapped_column("NUMERO_CERTIFICACION_ADQUISICION", Integer)

    # Relaciones
    sismografos: Mapped[list["SismografoORM"]] = relationship(
        back_populates="estacionSismologica",
        lazy="joined"
    )
