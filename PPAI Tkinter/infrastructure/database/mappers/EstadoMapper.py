from Entitys.STATE.Estado import Estado
from Entitys.STATE.PendienteDeRevision import PendienteDeRevision
from Entitys.STATE.Bloqueado import Bloqueado
from Entitys.STATE.Confirmado import Confirmado
from Entitys.STATE.Rechazado import Rechazado
from Entitys.STATE.Cerrado import Cerrado
from Entitys.STATE.PendienteDeCierre import PendienteDeCierre
from Entitys.STATE.AutoDetectado import AutoDetectado
from Entitys.STATE.AutoConfirmado import AutoConfirmado
from Entitys.STATE.EventoSinRevision import EventoSinRevision
from Entitys.STATE.Derivado import Derivado
from infrastructure.database.models.EstadoOrm import EstadoORM
from infrastructure.database.unit_of_work.uow_factory import uow_factory


class EstadoMapper:
    STATE_REGISTRY = {
        "PENDIENTE_DE_REVISION": PendienteDeRevision,
        "BLOQUEADO": Bloqueado,
        "CONFIRMADO": Confirmado,
        "RECHAZADO": Rechazado,
        "CERRADO": Cerrado,
        "PENDIENTE_DE_CIERRE": PendienteDeCierre,
        "AUTO_DETECTADO": AutoDetectado,
        "AUTO_CONFIRMADO": AutoConfirmado,
        "EVENTO_SIN_REVISION": EventoSinRevision,
        "DERIVADO": Derivado,
    }

    @staticmethod
    def toDomain(orm: EstadoORM) -> Estado:

        nombre = orm.nombre
        cls = EstadoMapper.STATE_REGISTRY.get(nombre)
        if cls is None:
            raise Exception(f"Estado {nombre} no existe")
        return cls()

    @staticmethod
    def toORM(state: Estado) -> EstadoORM:
        """Devuelve un EstadoORM con el nombre correspondiente a la subclase."""
        estadoId = EstadoMapper.get_id_por_nombre(state.nombre)
        return EstadoORM(nombre=state.nombre, estadoId=estadoId)

    @staticmethod
    def get_id_por_nombre(nombre: str) -> int:
        with uow_factory() as uow:
            session = uow.session
            found = session.query(EstadoORM).filter(EstadoORM.nombre == nombre).first()
            return found.estadoId