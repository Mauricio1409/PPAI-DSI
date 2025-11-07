from __future__ import annotations
from typing import Optional
from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.database.engine.base import Base


class EstadoORM(Base):
    __tablename__ = "ESTADO"

    estadoId: Mapped[int] = mapped_column("ESTADO_ID", Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[Optional[str]] = mapped_column("NOMBRE", Text)
