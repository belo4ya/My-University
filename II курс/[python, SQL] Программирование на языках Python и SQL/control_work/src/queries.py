from sqlalchemy.orm import Query
from sqlalchemy.sql import or_, func
from datetime import datetime
from pprint import pprint

from database import DataBase as db
from src.models import *
from utils import task


@task("2")
def second():
    """
    Напишите запрос, позволяющий получить из таблицы exam_marks
    значения столбца mark (экзаменационная оценка) для всех студентов,
    исключив из списка повторение одинаковых строк.
    """
    query: Query = db.session.query(
        ExamMark.mark
    ).distinct()
    pprint(query.all())


@task("3")
def third():
    """
    Напишите запрос для получения списка студентов
    без определенного места жительства.
    """
    query: Query = db.session.query(
        Student
    ).filter(
        Student.city.is_(None)
    )
    pprint(query.all())


@task("4")
def fourth():
    """
    Напишите запрос для получения списка студентов,
    проживающих в Воронеже и не получающих стипендию.
    """
    query: Query = db.session.query(
        Student
    ).filter(
        Student.city == 'Воронеж',
        or_(Student.stipend == 0, Student.stipend.is_(None))
    )
    pprint(query.all())


@task("5")
def fifth():
    """
    Напишите запрос для получения списка университетов,
    расположенных в Москве и имеющих рейтинг меньший, чем у НГУ.
    Значение рейтинга НГУ получите с помощью отдельного запроса или подзапроса.
    """
    ngu_rating = db.session.query(
        University.rating
    ).filter(
        University.name == 'НГУ'
    ).scalar()

    query: Query = db.session.query(
        University
    ).filter(
        University.city == 'Москва',
        University.rating < ngu_rating
    )

    pprint(query.all())


@task("6")
def sixth():
    """
    Напишите запрос, выполняющий вывод находящихся в таблице
    EXAM_MARKS номеров предметов обучения, экзамены по
    которым сдавались между 1 и 21 марта 2020 г.
    """
    query: Query = db.session.query(
        ExamMark.subject_id, ExamMark.date
    ).filter(
        ExamMark.date.between(datetime(2020, 3, 1), datetime(2020, 3, 21))
    )
    pprint(query.all())


@task("7")
def seventh():
    """
    Напишите запрос, который выполняет вывод названий
    предметов обучения, начинающихся на букву 'И'.
    """
    query: Query = db.session.query(
        Subject
    ).filter(
        Subject.name.startswith('И')
    )
    pprint(query.all())


@task("8")
def eighth():
    """
    Напишите запрос, выбирающий сведения о студентах,
    у которых имена начинаются на букву 'И' или 'С'.
    """
    query: Query = db.session.query(
        Student
    ).filter(
        or_(Student.first_name.startswith('И'), Student.first_name.startswith('С'))
    )
    pprint(query.all())


@task("9")
def ninth():
    """
    Напишите запрос для получения списка предметов обучения,
    названия которых состоят из более одного слова.
    """
    query: Query = db.session.query(
        Subject
    ).filter(
        Subject.name.like('% %')
    )
    pprint(query.all())


@task("10")
def tenth():
    """
    Напишите запрос для получения списка студентов,
    фамилии которых состоят из трех букв.
    """
    query: Query = db.session.query(
        Student
    ).filter(
        func.length(Student.last_name) == 3
    )
    pprint(query.all())


@task("11")
def eleventh():
    """
    Составьте запрос для таблицы STUDENT таким образом,
    чтобы получить результат в следующем виде.
    Распечатайте первые 9 записей результата.

    И. Иванов   1982-12-03
    П. Петров   1980-12-01
    В. Сидоров  1979-06-07
    """
    query: Query = db.session.query(
        Student.first_name, Student.last_name, Student.birthdate
    ).limit(9)
    pprint([f"{i[0][0]}. {i[1]}   {datetime.strftime(i[2], '%Y-%m-%d')}" for i in query.all()])


@task("12")
def twelve():
    """
    Напишите запрос для получения списка студентов,
    фамилии которых начинаются на ‘Ков’ или на ‘Куз’.
    """
    query: Query = db.session.query(
        Student
    ).filter(
        or_(Student.last_name.startswith('Ков'), Student.last_name.startswith('Куз'))
    )
    pprint(query.all())


@task("13")
def thirteenth():
    """
    Напишите запрос для получения списка предметов,
    названия которых оканчиваются на ‘ия’.
    """
    query: Query = db.session.query(
        Subject
    ).filter(
        Subject.name.endswith('ия')
    )
    pprint(query.all())


@task("14")
def fourteenth():
    """
    Напишите запрос для выбора из таблицы EXAM_MARKS записей,
    для которых отсутствуют значения оценок (поле MARK).
    """
    query: Query = db.session.query(
        ExamMark
    ).filter(
        ExamMark.mark.is_(None)
    )
    pprint(query.all())


@task("15")
def fifteenth():
    """
    Составьте запрос, выводящий фамилии, имена студентов и величину получаемых ими стипендий,
    при этом значения стипендий должны быть увеличены в 100 раз.
    """
    query: Query = db.session.query(
        Student.last_name, Student.first_name, Student.stipend * 100
    )
    pprint(query.all())


@task("16")
def sixteenth():
    """
    Составьте запрос для таблицы UNIVERSITY таким образом, чтобы выходная таблица
    содержала всего один столбец в следующем виде: Код-10; ВГУ-г.ВОРОНЕЖ; Рейтинг=296.
    """
    query: Query = db.session.query(
        University.id, University.name, University.city, University.rating
    )
    pprint([f"Код-{i[0]}; {i[1]}-г.{i[2].upper()}; Рейтинг={i[3]}." for i in query.all()])


@task("17")
def seventeenth():
    """
    Напишите запрос для подсчета количества студентов,
    сдававших экзамен по предмету обучения с идентификатором 10.
    """
    query: Query = db.session.query(
        ExamMark
    ).filter(
        ExamMark.subject_id == 10
    )
    pprint(query.count())


@task("18")
def eighteenth():
    """
    Напишите запрос, который позволяет подсчитать в таблице
    EXAM_MARKS количество различных предметов обучения.
    """
    query: Query = db.session.query(
        ExamMark.subject_id
    ).distinct()
    pprint(query.count())


@task("19")
def nineteenth():
    """
    Напишите запрос, который для каждого студента выполняет
    выборку его идентификатора и минимальной из полученных им оценок.
    """
    query: Query = db.session.query(
        Student, func.min(ExamMark.mark)
    ).join(ExamMark).group_by(
        ExamMark.student_id
    )
    pprint(query.all())


@task("20")
def twentieth():
    """
    Напишите запрос, который для каждого предмета обучения выводит
    наименование предмета и максимальное значение номера семестра,
    в котором этот предмет преподается.
    """
    query: Query = db.session.query(
        Subject.name, func.max(Subject.semester)
    ).group_by(
        Subject.name
    )
    pprint(query.all())


@task("21")
def twenty_first():
    """
    Напишите запрос, который для каждого конкретного дня сдачи экзамена
    выводит данные о количестве студентов, сдававших экзамен в этот день.
    """
    query: Query = db.session.query(
        ExamMark.date, func.count(ExamMark.student_id)
    ).group_by(
        ExamMark.date
    )
    pprint(query.all())


@task("22")
def twenty_second():
    """
    Напишите запрос, выдающий средний балл для каждого студента.
    """
    query: Query = db.session.query(
        Student, func.avg(ExamMark.mark)
    ).join(ExamMark).group_by(
        ExamMark.student_id
    )
    pprint(query.all())


@task("23")
def twenty_third():
    """
    Напишите запрос, выдающий средний балл для каждого экзамена.
    """
    query: Query = db.session.query(ExamMark)
    pprint(query.all())


if __name__ == '__main__':
    second()
    third()
    fourth()
    fifth()
    sixth()
    seventh()
    eighth()
    ninth()
    tenth()
    eleventh()
    twelve()
    thirteenth()
    fourteenth()
    fifteenth()
    sixteenth()
    seventeenth()
    eighteenth()
    nineteenth()
    twentieth()
    twenty_first()
    twenty_second()
    twenty_third()
