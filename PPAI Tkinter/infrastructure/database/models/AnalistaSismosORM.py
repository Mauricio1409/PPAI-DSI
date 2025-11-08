from __future__ import annotations

from typing import Optional


from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.engine.base import Base





class AnalistaSismosORM(Base):
    __tablename__ = "ANALISTA_SISMOS"

    analistaId: Mapped[int] = mapped_column("ANALISTA_ID", Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[Optional[str]] = mapped_column("NOMBRE", Text)
    apellido: Mapped[Optional[str]] = mapped_column("APELLIDO", Text)



