from infrastructure.database.repositories.SesionRepository import SesionRepository

from data import sesion1

repo = SesionRepository()

print(repo.get_all())

repo.save(sesion1)

print("se creo un nuevo registro")
print(repo.get_all())