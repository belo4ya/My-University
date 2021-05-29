from datetime import datetime
from pprint import pprint

from sqlalchemy import cast, Integer
from sqlalchemy.sql import select, Select, or_, func

from database import DataBase as db
from src.models import *
from utils import task


@task("2")
def second():
    """
    Напишите запрос, позволяющий получить из таблицы exam_marks
    значения столбца mark (экзаменационная оценка) для всех студентов,
    исключив из списка повторение одинаковых строк.
    Результат не должен содержать значений (None).
    Упорядочить результат по возрастанию значения оценки.
    """
    stmt: Select = select(
        ExamMark.mark
    ).distinct().where(
        ExamMark.mark.isnot(None)
    ).order_by(
        ExamMark.mark
    )

    pprint(db.fetch_scalars(stmt))


@task("3")
def third():
    """
    Напишите запрос для получения списка студентов без определенного места жительства.
    Результат должен содержать идентификатор студента, фамилию, имя.
    """
    stmt: Select = select(
        Student.id, Student.last_name, Student.first_name
    ).where(
        Student.city.is_(None)
    )

    pprint(db.fetch_all(stmt))


@task("4")
def fourth():
    """
    Напишите запрос для получения списка студентов,
    проживающих в Воронеже и не получающих стипендию.
    """
    stmt: Select = select(
        Student
    ).where(
        Student.city == 'Воронеж',
        or_(Student.stipend == 0, Student.stipend.is_(None))
    )

    pprint(db.fetch_all(stmt))


@task("5")
def fifth():
    """
    Напишите запрос для получения списка университетов,
    расположенных в Москве и имеющих рейтинг меньший, чем у НГУ.
    Значение рейтинга НГУ получите с помощью отдельного запроса или подзапроса.
    """
    ngu_rating = db.fetch_scalar(select(
        University.rating
    ).where(
        University.name == 'НГУ'
    ))

    stmt: Select = select(
        University
    ).where(
        University.city == 'Москва',
        University.rating < ngu_rating
    )

    pprint(db.fetch_all(stmt))


@task("6")
def sixth():
    """
    Напишите запрос, выполняющий вывод находящихся в таблице
    EXAM_MARKS номеров предметов обучения, экзамены по
    которым сдавались между 1 и 21 марта 2020 г.
    """
    stmt: Select = select(
        ExamMark.subject_id, ExamMark.date
    ).where(
        ExamMark.date.between(datetime(2020, 3, 1), datetime(2020, 3, 21))
    )

    pprint(db.fetch_all(stmt))


@task("7")
def seventh():
    """
    Напишите запрос, который выполняет вывод названий
    предметов обучения, начинающихся на букву 'И'.
    """
    stmt: Select = select(
        Subject.name
    ).where(
        Subject.name.startswith('И')
    )

    pprint(db.fetch_all(stmt))


@task("8")
def eighth():
    """
    Напишите запрос, выбирающий сведения о студентах,
    у которых имена начинаются на букву 'И' или 'С'.
    """
    stmt: Select = select(
        Student
    ).where(
        or_(Student.first_name.startswith('И'), Student.first_name.startswith('С'))
    )

    pprint(db.fetch_all(stmt))


@task("9")
def ninth():
    """
    Напишите запрос для получения списка предметов обучения,
    названия которых состоят из более одного слова.
    """
    stmt: Select = select(
        Subject
    ).where(
        Subject.name.like('% %')
    )

    pprint(db.fetch_all(stmt))


@task("10")
def tenth():
    """
    Напишите запрос для получения списка студентов,
    фамилии которых состоят из трех букв.
    """
    stmt: Select = select(
        Student
    ).where(
        func.length(Student.last_name) == 3
    )

    pprint(db.fetch_all(stmt))


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
    stmt: Select = select(
        Student.first_name, Student.last_name, Student.birthdate
    ).limit(9)

    pprint([f"{i[0][0]}. {i[1]}   {datetime.strftime(i[2], '%Y-%m-%d')}" for i in db.fetch_all(stmt)])


@task("12")
def twelve():
    """
    Напишите запрос для получения списка студентов,
    фамилии которых начинаются на ‘Ков’ или на ‘Куз’.
    """
    stmt: Select = select(
        Student
    ).where(
        or_(Student.last_name.startswith('Ков'), Student.last_name.startswith('Куз'))
    )

    pprint(db.fetch_all(stmt))


@task("13")
def thirteenth():
    """
    Напишите запрос для получения списка предметов,
    названия которых оканчиваются на ‘ия’.
    """
    stmt: Select = select(
        Subject
    ).where(
        Subject.name.endswith('ия')
    )

    pprint(db.fetch_all(stmt))


@task("14")
def fourteenth():
    """
    Составьте запрос, выводящий фамилии, имена студентов и величину получаемых ими стипендий,
    при этом значения стипендий должны быть увеличены в 100 раз.
    Распечатайте первые 10 результатов.
    """
    stmt: Select = select(
        Student.last_name, Student.first_name, Student.stipend * 100
    ).limit(10)

    pprint(db.fetch_all(stmt))


@task("15")
def fifteenth():
    """
    Составьте запрос для таблицы UNIVERSITY таким образом, чтобы выходная таблица
    содержала всего один столбец в следующем виде: Код-10; ВГУ-г.ВОРОНЕЖ; Рейтинг=296.
    """
    stmt: Select = select(
        University.id, University.name, University.city, University.rating
    )

    pprint([f"Код-{i[0]}; {i[1]}-г.{i[2].upper()}; Рейтинг={i[3]}." for i in db.fetch_all(stmt)])


@task("16")
def sixteenth():
    """
    Напишите запрос для подсчета количества студентов,
    сдававших экзамен по предмету обучения с идентификатором 10.
    """
    stmt: Select = select(
        func.count(ExamMark.subject_id)
    ).where(
        ExamMark.subject_id == 10
    )

    pprint(db.fetch_scalar(stmt))


@task("17")
def seventeenth():
    """
    Напишите запрос, который позволяет подсчитать в таблице
    EXAM_MARKS количество различных предметов обучения.
    """
    stmt: Select = select(
        ExamMark.subject_id
    ).distinct()

    pprint(len(db.fetch_all(stmt)))


@task("18")
def eighteenth():
    """
    Напишите запрос, который для каждого студента выполняет
    выборку его идентификатора и минимальной из полученных им оценок.
    """
    stmt: Select = select(
        ExamMark.student_id, func.min(ExamMark.mark)
    ).group_by(
        ExamMark.student_id
    )

    pprint(db.fetch_all(stmt))


@task("19")
def nineteenth():
    """
    Напишите запрос, который для каждого конкретного дня сдачи
    экзамена выводит данные о количестве студентов,
    сдававших экзамен в этот день.
    """
    stmt: Select = select(
        ExamMark.date, func.count(ExamMark.student_id)
    ).group_by(
        ExamMark.date
    )

    pprint(db.fetch_all(stmt))


@task("20")
def twentieth():
    """
    Напишите запрос, выдающий идентификатор студента и его средний балл.
    """
    stmt: Select = select(
        ExamMark.student_id, func.avg(ExamMark.mark)
    ).group_by(
        ExamMark.student_id
    )

    pprint(db.fetch_all(stmt))


@task("21")
def twenty_first():
    """
    Напишите запрос, выдающий средний балл для каждого экзамена.
    """
    stmt: Select = select(
        Subject, func.avg(ExamMark.mark)
    ).join(Subject).group_by(
        ExamMark.subject_id
    )

    pprint(db.fetch_all(stmt))


@task("22")
def twenty_second():
    """
    Напишите запрос, определяющий количество сдававших
    студентов для каждого предмета, по которому был экзамен.
    """
    stmt: Select = select(
        Subject, func.count(ExamMark.student_id)
    ).join(ExamMark).group_by(
        ExamMark.subject_id
    )

    pprint(db.fetch_all(stmt))


@task("23")
def twenty_third():
    """
    Напишите запрос для определения количества предметов,
    изучаемых на каждом курсе.
    """
    course = cast(Subject.semester + 1, Integer) / 2
    stmt: Select = select(
        course, func.count(Subject.id)
    ).group_by(
        course
    )

    pprint(db.fetch_all(stmt))


@task("24")
def twenty_fourth():
    """
    Для каждого университета напишите запрос,
    выводящий суммарную стипендию обучающихся в нем студентов,
    с последующей сортировкой списка по этому значению.
    """
    stmt: Select = select(
        University, func.sum(Student.stipend)
    ).join(Student).group_by(
        Student.university_id
    )

    pprint(db.fetch_all(stmt))


@task("25")
def twenty_fifth():
    """
    Для каждого студента напишите запрос, выводящий идентификатор студента
    и среднее значение оценок, полученных им на всех экзаменах.
    """
    stmt: Select = select(
        ExamMark.student_id, func.avg(ExamMark.mark)
    ).group_by(
        ExamMark.student_id
    )

    pprint(db.fetch_all(stmt))


@task("26")
def twenty_sixth():
    """
    Напишите запрос, выводящий количество студентов, проживающих в каждом городе.
    Список отсортировать в порядке убывания количества студентов.
    """
    stmt: Select = select(
        Student.city, func.count(Student.id)
    ).group_by(Student.city)

    pprint(db.fetch_all(stmt))


@task("extra_students")
def extra_students():
    """
    Подзапрос для получения всех студентов,
    обучающихся в своем городе
    """
    sub: Select = select(
        University.city
    ).where(
        University.id == Student.university_id
    ).scalar_subquery()

    stmt: Select = select(
        Student
    ).where(
        Student.city == sub
    )

    pprint(db.fetch_all(stmt))


@task("extra_lecturers")
def extra_lecturers():
    """
    Подзапрос для получения информации об преподавателях,
    работающих не в своем городе
    """
    sub: Select = select(
        University.city
    ).where(
        University.id == Lecturer.university_id
    ).scalar_subquery()

    stmt: Select = select(
        Lecturer
    ).where(
        Lecturer.city != sub
    )

    pprint(db.fetch_all(stmt))


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
    twenty_fourth()
    twenty_fifth()
    twenty_sixth()
    extra_students()
    extra_lecturers()
