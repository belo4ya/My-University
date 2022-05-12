from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy.sql import Select

from src.models import Base


class DataBase:
    DATABASE = "sqlite"
    DB_NAME = "resources/students.db"
    engine: Engine = create_engine(f"{DATABASE}:///{DB_NAME}", echo=False)
    session: Session = sessionmaker(bind=engine)()

    @staticmethod
    def fetch_all(statement: Select) -> list:
        with DataBase.engine.connect() as connection:
            return connection.execute(statement).all()

    @staticmethod
    def fetch_one(statement: Select):
        with DataBase.engine.connect() as connection:
            return connection.execute(statement).one()

    @staticmethod
    def fetch_scalar(statement: Select):
        with DataBase.engine.connect() as connection:
            return connection.execute(statement).scalar_one()

    @staticmethod
    def fetch_scalars(statement: Select):
        with DataBase.engine.connect() as connection:
            return connection.execute(statement).scalars().all()


if __name__ == '__main__':
    Base.metadata.create_all(DataBase.engine)
