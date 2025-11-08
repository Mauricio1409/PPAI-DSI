from data import eventosSismicos
from infrastructure.database.repositories.EventoSismicoRepository import EventoSismicoRepository

repo = EventoSismicoRepository()

for evento in eventosSismicos:
    repo.save(evento)

print("se crearon los registros de EventosSismicos y toda su jerarquía")

print("se obtiene todos los registros")
print(repo.get_all())