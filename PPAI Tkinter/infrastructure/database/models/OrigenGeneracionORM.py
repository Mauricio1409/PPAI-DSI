from __future__ import annotations
from typing import Optional
from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.database.engine.base import Base


class OrigenGeneracionORM(Base):
    __tablename__ = "ORIGEN_GENERACION"

    origenGeneracionId: Mapped[int] = mapped_column("ORIGEN_GENERACION_ID", Integer, primary_key=True, autoincrement=True)
    descripcion: Mapped[Optional[str]] = mapped_column("DESCRIPCION", Text)
    nombre: Mapped[Optional[str]] = mapped_column("NOMBRE", Text)
