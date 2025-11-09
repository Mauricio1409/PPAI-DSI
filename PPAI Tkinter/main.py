from datetime import datetime

from Boundarys.PantNuevoEventoSismico import VentanaPantNuevoEventoSismico
from Entitys.Sesion import Sesion

from infrastructure.database.repositories.SesionRepository import SesionRepository
from infrastructure.database.repositories.UsuarioRepository import UsuarioRepository


def start_program():
    print('-'*100)
    print("ejecutando programa....")
    print('-'*100)

    user_repo = UsuarioRepository()
    sesion_repo = SesionRepository()

    usuario1 = user_repo.get_by_id(1)

    print('-'*100)
    print("Creando Sesion para el usuario:", usuario1.nombre)
    sesion1 = Sesion(None, usuario1, datetime.now(), None)

    sesion_repo.save(sesion1)
    print()
    print("Sesion creada con éxito.")
    print('-'*100)

    try:

        v1 = VentanaPantNuevoEventoSismico()
        v1.opcionRegistrarRevisionManual()
        v1.mainloop()

        print("\n"*4)
        print('-'*100)
        print("Ejecución finalizada.")
    except Exception as e:
        raise e
    finally:
        sesion_actual = sesion_repo.get_actual()
        sesion_actual.fechaHoraFin = datetime.now()
        sesion_repo.save(sesion_actual)
        print()
        print("Sesion Cerrada")
        print('-'*100)


if __name__ == "__main__":
    start_program()