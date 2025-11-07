from __future__ import annotations
from typing import Optional
from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.database.engine.base import Base


class MagnitudRitcherORM(Base):
    __tablename__ = "MAGINTUD_RITCHER"

    magnitudRitcherId: Mapped[int] = mapped_column("MAGNITUD_RITCHER_ID", Integer, primary_key=True, autoincrement=True)
    descripcionMagnitud: Mapped[Optional[str]] = mapped_column("DESCRIPCION_MAGNITUD", Text)
    numero: Mapped[Optional[int]] = mapped_column("NUMERO", Integer)
