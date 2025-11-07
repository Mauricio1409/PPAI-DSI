from __future__ import annotations
from typing import Optional
from decimal import Decimal
from sqlalchemy import Integer, Text, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.database.engine.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from infrastructure.database.models.DetalleMuestraSismicaORM import DetalleMuestraSismicaORM

class TipoDatoORM(Base):
    __tablename__ = "TIPO_DATO"

    tipoDatoId: Mapped[int] = mapped_column("TIPO_DATO_ID", Integer, primary_key=True, autoincrement=True)
    denominacion: Mapped[Optional[str]] = mapped_column("DENOMINACION", Text)
    unidadMedida: Mapped[Optional[str]] = mapped_column("UNIDAD_MEDIDA", Text)
    valorUmbral: Mapped[Optional[Decimal]] = mapped_column("VALOR_UMBRAL", Numeric)

    detallesMuestras: Mapped[list["DetalleMuestraSismicaORM"]] = relationship(
        back_populates="tipoDato",
        lazy="joined"
    )
