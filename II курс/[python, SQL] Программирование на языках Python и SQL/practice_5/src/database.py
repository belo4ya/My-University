from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import sessionmaker, Session


class DataBase:
    DATABASE = "sqlite"
    DB_NAME = "university_life.db"
    engine: Engine = create_engine(f"{DATABASE}:///{DB_NAME}")
    session: Session = sessionmaker(bind=engine)()
