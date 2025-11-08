from sqlalchemy.orm import sessionmaker
from infrastructure.database.engine.engine import create_db_engine
from infrastructure.database.unit_of_work.unit_of_work import SqlAlchemyUnitOfWork

engine = create_db_engine()

session_local = sessionmaker(bind=engine)

def uow_factory():
    return SqlAlchemyUnitOfWork(session_local)