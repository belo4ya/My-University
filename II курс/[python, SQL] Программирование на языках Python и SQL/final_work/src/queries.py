from pprint import pprint

from sqlalchemy.sql import select, Select, func

from src.database import DataBase as db
from src.models import *
from src.utils import task


@task("10")
def task_10():
    """
    Напишите запрос для сортировки списка университетов по значениям
    максимальной стипендии, выплачиваемой студентам
    """
    max_stipend = func.max(Student.stipend)
    stmt: Select = select(
        University.name, max_stipend
    ).join(Student).group_by(
        University.id
    ).order_by(
        max_stipend.desc()
    )

    print(stmt)
    print('\n')
    pprint(db.fetch_all(stmt))


@task("16")
def task_16():
    """
    Напишите запрос, который выполняет выборку фамилий ВСЕХ студентов,
    с указанием для студентов, сдававших экзамены, идентификаторов сданных ими предметов обучения.
    """
    stmt: Select = select(
        Student.last_name, ExamMark.subject_id
    ).join(ExamMark, isouter=True)

    print(stmt)
    print('\n')
    pprint(db.fetch_all(stmt))
