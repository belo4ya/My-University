import pandas as pd
import pprint
from src.models import University, Student, Subject, ExamMark, ActivityLecturer, SubjectLecturer
from src.database import DataBase


def create():
    # сбор данных
    university: pd.DataFrame = pd.read_excel("./resources/educational_activities_university.xlsx")
    subject: pd.DataFrame = pd.read_excel("./resources/educational_activities_subject.xlsx")
    student: pd.DataFrame = pd.read_excel("./resources/educational_activities_student.xlsx")
    exam_mark: pd.DataFrame = pd.read_excel("./resources/educational_activities_exam_marks.xlsx")
    activity_lecturer: pd.DataFrame = pd.read_excel("./resources/educational_activities_lecturer.xlsx")
    subject_lecturer: pd.DataFrame = pd.read_excel("./resources/educational_activities_subj_lect.xlsx")

    # предобработка и очистка данных
    university.rename(columns={"UNIV_ID": "id", "UNIV_NAME": "name",
                               "RATING": "rating", "CITY": "city"}, inplace=True)
    subject.rename(columns={"SUBJ_ID": "id", "SUBJ_NAME": "name",
                            "HOUR": "hour", "SEMESTER": "semester"}, inplace=True)
    student.rename(columns={"STUDENT_ID": "id", "SURNAME": "last_name",
                            "NAME": "first_name", "STIPEND": "stipend",
                            "KURS": "course", "CITY": "city",
                            "BIRTHDAY": "birthdate", "UNIV_ID": "university_id"}, inplace=True)
    exam_mark.rename(columns={"EXAM_ID": "id",
                              "STUDENT_ID": "student_id",
                              "SUBJ_ID": "subject_id",
                              "MARK": "mark",
                              "EXAM_DATE": "date"}, inplace=True)
    activity_lecturer.rename(columns={"LECTURER_ID": "id", "SURNAME": "first_name",
                                      "NAME": "last_name", "CITY": "city",
                                      "UNIV_ID": "university_id"}, inplace=True)
    subject_lecturer.rename(columns={"LECTURER_ID": "lecturer_id", "SUBJ_ID": "subject_id"}, inplace=True)

    student["birthdate"] = pd.to_datetime(student["birthdate"])
    exam_mark["date"] = pd.to_datetime(exam_mark["date"])

    # выгрузка в БД
    db = DataBase()
    university.to_sql(University.__tablename__, con=db.engine, if_exists="append", index=False)
    subject.to_sql(Subject.__tablename__, con=db.engine, if_exists="append", index=False)
    student.to_sql(Student.__tablename__, con=db.engine, if_exists="append", index=False)
    exam_mark.to_sql(ExamMark.__tablename__, con=db.engine, if_exists="append", index=False)
    activity_lecturer.to_sql(ActivityLecturer.__tablename__, con=db.engine, if_exists="append", index=False)
    subject_lecturer.to_sql(SubjectLecturer.__tablename__, con=db.engine, if_exists="append", index=False)


def show():
    db = DataBase()
    pprint.pprint(db.select_student())
    pprint.pprint(db.select_subject_lecturer())
    pprint.pprint(db.select_subject())
    pprint.pprint(db.select_university())
    pprint.pprint(db.select_exam_mark())
    pprint.pprint(db.select_activity_lecturer())


if __name__ == '__main__':
    DataBase()._remove_all_tables()  # удалит все таблицы
    DataBase()._create_all_tables()  # создаст все таблицы заново
    create()  # наполнение таблиц данными
    show()  # отчет
