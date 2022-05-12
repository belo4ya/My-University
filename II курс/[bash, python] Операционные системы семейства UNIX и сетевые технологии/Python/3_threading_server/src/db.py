import datetime

from sqlalchemy import (Column, Integer, String, DateTime)
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm.session import sessionmaker, Session


@as_declarative()
class Base(object):
    id = Column(Integer(), primary_key=True, autoincrement=True)


class User(Base):
    __tablename__ = "USERS"

    username = Column(String(80), nullable=False, unique=True)
    password = Column(String(80), nullable=False)

    session_start = Column(DateTime, default=datetime.datetime.now())
    session_token = Column(String(80), nullable=True)

    def __repr__(self):
        return f"User(" \
               f"id='{self.id}', " \
               f"username='{self.username}'" \
               f")"


class DataBase:
    DATABASE = "sqlite"
    DB_NAME = "users.sqlite3"
    engine: Engine = create_engine(f"{DATABASE}:///{DB_NAME}", echo=False)
    session: Session = sessionmaker(bind=engine, autocommit=True)()


if __name__ == '__main__':
    Base.metadata.create_all(DataBase.engine)
