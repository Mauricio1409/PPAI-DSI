from sqlalchemy.orm import sessionmaker
from infrastructure.database.engine.engine import create_db_engine

engine = create_db_engine()

session_local = sessionmaker(bind=engine)

def uow_factory():
    return