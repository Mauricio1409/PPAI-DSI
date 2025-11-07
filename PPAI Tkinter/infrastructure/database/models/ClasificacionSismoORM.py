from __future__ import annotations
from typing import Optional
from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.database.engine.base import Base


class ClasificacionSismoORM(Base):
    __tablename__ = "CLASIFICACION_SISMO"

    clasificacionSismoId: Mapped[int] = mapped_column("CLASIFICACION_SISMO_ID", Integer, primary_key=True, autoincrement=True)
    kmProfundidadHasta: Mapped[Optional[int]] = mapped_column("KM_PROFUNDIDAD_HASTA", Integer)
    kmProfundidadDesde: Mapped[Optional[int]] = mapped_column("KM_PROFUNDIDAD_DESDE", Integer)
    nombre: Mapped[Optional[str]] = mapped_column("NOMBRE", Text)
