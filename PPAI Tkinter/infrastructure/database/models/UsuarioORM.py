from __future__ import annotations

from typing import Optional, List


from sqlalchemy import Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.engine.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from infrastructure.database.models.AnalistaSismosORM import AnalistaSismosORM
    from infrastructure.database.models.SesionORM import SesionORM

class UsuarioORM(Base):
    __tablename__ = "USUARIO"

    usuarioId: Mapped[int] = mapped_column("USUARIO_ID", Integer, primary_key=True, autoincrement=True)
    contrasena: Mapped[Optional[str]] = mapped_column("CONTRASENA", Text)
    nombre: Mapped[Optional[str]] = mapped_column("NOMBRE", Text)
    analistaId: Mapped[Optional[int]] = mapped_column(
        "ANALISTA_ID",
        ForeignKey("ANALISTA_SISMOS.ANALISTA_ID"),
        nullable=True
    )

    # Relaciones
    analista: Mapped[Optional["AnalistaSismosORM"]] = relationship(
        back_populates="usuarios",
        lazy="joined"
    )
    sesiones: Mapped[List["SesionORM"]] = relationship(
        back_populates="usuario",
        lazy="joined"
    )


