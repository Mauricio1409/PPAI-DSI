from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.engine.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from infrastructure.database.models.UsuarioORM import UsuarioORM

class SesionORM(Base):
    __tablename__ = 'SESION'

    sesionId: Mapped[int] = mapped_column('SESION_ID', Integer, primary_key=True, autoincrement=True)
    usuarioId: Mapped[Optional[int]] = mapped_column(
        'USUARIO_ID',
        ForeignKey('USUARIO.USUARIO_ID'),
        nullable=True
    )
    # En SQLite estos campos están como TEXT; los mapeo a DateTime sin TZ.
    # SQLAlchemy serializa/deserializa a TEXT en SQLite sin problema.
    fechaHoraInicio: Mapped[Optional[datetime]] = mapped_column('FECHA_HORA_INICIO', DateTime(timezone=False))
    fechaHoraFin: Mapped[Optional[datetime]] = mapped_column('FECHA_HORA_FIN', DateTime(timezone=False))

    # Relaciones
    usuario: Mapped[Optional['UsuarioORM']] = relationship(
        lazy="joined"
    )