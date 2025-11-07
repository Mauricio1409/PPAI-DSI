from __future__ import annotations
from typing import Optional
from decimal import Decimal
from sqlalchemy import Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.database.engine.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from infrastructure.database.models.TipoDatoORM import TipoDatoORM
    from infrastructure.database.models.MuestraSismicaORM import MuestraSismicaORM

class DetalleMuestraSismicaORM(Base):
    __tablename__ = "DETALLE_MUESTRA_SISMICA"

    detalleMuestraSismicaId: Mapped[int] = mapped_column("DETALLE_MUESTRA_SISMICA_ID", Integer, primary_key=True, autoincrement=True)
    valor: Mapped[Optional[Decimal]] = mapped_column("VALOR", Numeric)
    muestraSismicaId: Mapped[int] = mapped_column(
        "MUESTRA_SISMICA_ID",
        ForeignKey("MUESTRA_SISMICA.MUESTRA_SISMICA_ID"),
        nullable=False
    )
    tipoDatoId: Mapped[int] = mapped_column(
        "TIPO_DATO_ID",
        ForeignKey("TIPO_DATO.TIPO_DATO_ID"),
        nullable=False
    )

    muestraSismica: Mapped["MuestraSismicaORM"] = relationship(
        back_populates="detalles",
        lazy="joined"
    )
    tipoDato: Mapped["TipoDatoORM"] = relationship(
        back_populates="detallesMuestras",
        lazy="joined"
    )
