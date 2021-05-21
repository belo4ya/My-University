import pandas as pd
from sqlalchemy.orm import Query
from sqlalchemy.sql import func

from src.utils import answer
from src.database import DataBase
from src.models import *

db = DataBase()


def create_dataframe(result_list):
    keys = result_list[0].keys()
    result = {k: [] for k in keys}
    for raw in result_list:
        for i, k in enumerate(keys):
            result[k].append(raw[i])

    return pd.DataFrame(result)


def ninth() -> pd.DataFrame:
    """
    Напишите запрос для подсчета количества студентов , сдававших экзамен
    по предмету обучения с идентификатором, равным 20.
    """
    query: Query = db.session.query(ExamMark).filter(ExamMark.subject_id == 20)
    return pd.DataFrame({"COUNT": [query.count(), ]})


def tenth() -> pd.DataFrame:
    """
    Напишите запрос, который позволяет подсчитать в таблице EXAM_MARKS
    количество различных предметов обучения.
    """
    query: Query = db.session.query(ExamMark).group_by(ExamMark.subject_id)
    return pd.DataFrame({"COUNT": [query.count(), ]})


def eleventh() -> pd.DataFrame:
    """
    Напишите запрос, который выполняет выборку для каждого студента
    значения его идентификатора и минимальной из полученных им оценок.
    """
    query: Query = db.session.query(
        ExamMark.student_id,
        func.min(ExamMark.mark).label("MIN_MARK")
    ).group_by(ExamMark.student_id)

    return create_dataframe(query.all())


def twelve() -> pd.DataFrame:
    """
    Напишите запрос, который выполняет выборку для каждого студента
    значения его идентификатора и максимальной из полученных им оценок.
    """
    query: Query = db.session.query(
        ExamMark.student_id,
        func.max(ExamMark.mark).label("MAX_MARK")
    ).group_by(ExamMark.student_id)

    return create_dataframe(query.all())


def thirteenth() -> pd.DataFrame:
    """
    Напишите запрос, выполняющий вывод фамилии первого в алфавитном
    порядке (по фамилии) студента, фамилия которого начинается на букву “И”.
    """
    query: Query = (db.session.query(Student.last_name)
                    .filter(Student.last_name.ilike("И%"))
                    .order_by(Student.last_name))
    return pd.DataFrame({Student.last_name: [query.first().last_name, ]})


def fourteenth() -> pd.DataFrame:
    """
    Напишите запрос, который выполняет вывод для каждого предмета
    обучения на именование предмета и максимальное значение номера
    семестра, в котором этот предмет преподается.
    """
    query: Query = db.session.query(
        Subject.name,
        func.max(Subject.semester).label("MAX")
    ).group_by(Subject.id)
    return create_dataframe(query.all())


def fifteenth() -> pd.DataFrame:
    """
    Напишите запрос, который выполняет вывод данных для каждого
    конкретного дня сдачи экзамена о количестве студентов, сдававших
    экзамен в этот день.
    """
    query: Query = db.session.query(
        ExamMark.date,
        func.count(func.distinct(ExamMark.student_id)).label("COUNT_STUDENTS")
    ).group_by(ExamMark.date)
    return create_dataframe(query.all())


def sixteenth() -> pd.DataFrame:
    """
    Напишите запрос для получения среднего балла
    для каждого курса по каждому предмету.
    """
    query: Query = (db.session.query(Student.course,
                                     ExamMark.subject_id,
                                     func.avg(ExamMark.mark).label("AVG(MARK)"))
                    .join(Student)
                    .group_by(Student.course, ExamMark.subject_id)
                    .order_by(Student.course, ExamMark.subject_id))
    return create_dataframe(query.all())


def seventeenth() -> pd.DataFrame:
    """
    Напишите запрос для получения среднего балла для каждого студента.
    """
    query: Query = db.session.query(
        ExamMark.student_id,
        func.avg(ExamMark.mark).label("AVG(MARK)")
    ).group_by(ExamMark.student_id)
    return create_dataframe(query.all())


def eighteenth() -> pd.DataFrame:
    """
    Напишите запрос для получения среднего балла для каждого экзамена.
    """
    query: Query = db.session.query(
        ExamMark.id,
        func.avg(ExamMark.mark).label("AVG(MARK)")
    ).group_by(ExamMark.id)
    return create_dataframe(query.all())


def nineteenth() -> pd.DataFrame:
    """
    Напишите запрос для определения количества студентов, сдававших каждый экзамен
    """
    query: Query = db.session.query(
        ExamMark.id,
        func.count(ExamMark.student_id).label("COUNT(STUDENT_ID)")
    ).group_by(ExamMark.id)
    return create_dataframe(query.all())


def twentieth() -> pd.DataFrame:
    """
    Напишите запрос для определения количества изучаемых предметов на каждом курсе
    """
    course = func.round((Subject.semester + 1) / 2).label("COURSE")
    query: Query = db.session.query(
        course,
        func.count(Subject.id).label("COUNT(SUBJECT_ID)")
    ).group_by(course)
    return create_dataframe(query.all())


if __name__ == '__main__':
    answer(9, ninth())
    answer(10, tenth())
    answer(11, eleventh())
    answer(12, twelve())
    answer(13, thirteenth())
    answer(14, fourteenth())
    answer(15, fifteenth())
    answer(16, sixteenth())
    answer(17, seventeenth())
    answer(18, eighteenth())
    answer(19, nineteenth())
    answer(20, twentieth())
