from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import sessionmaker, Session

from src.models import *


class DataBase:
    DATABASE = "sqlite"
    DB_NAME = "resources/pay.db"
    engine: Engine = create_engine(f"{DATABASE}:///{DB_NAME}", echo=False)
    session: Session = sessionmaker(bind=engine, autocommit=True)()

    @classmethod
    def init_data(cls):
        with cls.session.begin():
            my_bank = Bank(id=1, name="AwesomeBank", balance=24_000_000)
            me = Client(first_name="Alexey", last_name="Kovalev", account_balance=my_bank.id)

            other_bank = Bank(id=2, name="NoBank", balance=117.52)
            other = Client(first_name="Павел", last_name="Чичиков", account_balance=other_bank.id)

            cls.session.add_all([my_bank, me, other_bank, other])

    @classmethod
    def create_all(cls):
        Base.metadata.create_all(cls.engine)


if __name__ == '__main__':
    DataBase.create_all()
    DataBase.init_data()