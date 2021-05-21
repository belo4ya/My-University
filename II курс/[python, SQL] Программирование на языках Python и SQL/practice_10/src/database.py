from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import sessionmaker, Session
from .models import Base


class DataBase:
    DATABASE = "sqlite"
    DB_NAME = "resources/listings.db"
    engine: Engine = create_engine(f"{DATABASE}:///{DB_NAME}", echo=False)
    session: Session = sessionmaker(bind=engine)()


if __name__ == '__main__':
    Base.metadata.create_all(DataBase.engine)
