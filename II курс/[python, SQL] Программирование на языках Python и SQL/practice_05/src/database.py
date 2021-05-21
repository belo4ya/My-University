from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import sessionmaker, Session
from datetime import datetime

from src.models import *


class DataBase:
    DATABASE = "sqlite"
    DB_NAME = "../resources/university_life.db"
    engine: Engine = create_engine(f"{DATABASE}:///{DB_NAME}", echo=False)
    # engine: Engine = create_engine("mysql://root:1234@localhost/educational_activities?host=localhost?port=3306")
    session: Session = sessionmaker(bind=engine)()

    @staticmethod
    def init_ascii_data():
        DataBase.session.add(ActivityLecturer(first_name="Sokolov", last_name="Petr",
                                              city="Moscow", university_id=22))
        DataBase.session.add(Student(first_name="Alexey", last_name="Kovalev", stipend=2925, course=2,
                                     city="Troitsky", birthdate=datetime(2001, 9, 14), university_id=22))
        DataBase.session.add(Subject(name="Python", hour=40, semester=4))
        DataBase.session.add(University(name="FinUniv", rating=100, city="Moscow"))
        DataBase.session.commit()
