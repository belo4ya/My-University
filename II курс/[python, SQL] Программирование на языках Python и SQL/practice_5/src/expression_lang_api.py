from sqlalchemy import select, cast, VARCHAR
from sqlalchemy.sql import func, and_
from sqlalchemy.sql.elements import BinaryExpression, Cast
import pandas as pd

from src.utils import answer
from src.database import DataBase
from src.models import *

pd.set_option('display.max_colwidth', None)

db = DataBase()
F_DATE = "<<f-date>>"
F_DIGIT = "<<f-digit>>"


def as_string(col) -> Cast:
    return cast(col, VARCHAR)


def concat_ws(sep: str, *args) -> BinaryExpression:
    cols = list(map(as_string, args))
    query = ""
    for i in range(len(cols)):
        query += cols[i]
        if i != len(cols) - 1:
            query += sep

    return query


def not_null(*args):
    return and_(*[col.isnot(None) for col in args])


def first() -> pd.DataFrame:
    """
    Составьте запрос для таблицы STUDENT таким образом, чтобы выходная
    таблица содержала один столбец, содержащий последовательность
    разделенных символом “;” (точка с запятой) значений всех столбцов этой
    таблицы, и при этом текстовые значения должны отображаться
    прописными символами (верхний регистр), то есть быть
    представленными в следующем виде:
    10;КУЗНЕЦОВ;БОРИС;0;БРЯНСК;8/12/1981;10.
    """
    label = "RESULT"
    query = func.upper(concat_ws(
        ";",
        Student.id,
        Student.last_name,
        Student.first_name,
        Student.stipend,
        Student.city,
        F_DATE,
        as_string(Student.university_id) + "."
    )).label(label)
    query = select([query, Student.birthdate]).where(not_null(*Student.c))

    result_proxy = db.session.execute(query)
    result = [
        (raw[0].replace(F_DATE.upper(), raw[1].strftime("%#d/%m/%Y"))).upper()
        for raw in result_proxy
    ]
    return pd.DataFrame({label: result})


def second() -> pd.DataFrame:
    """
    Составьте запрос для таблицы STUDENT таким образом, чтобы выходная
    таблица содержала всего один столбец в следующем виде:
    Б.КУЗНЕЦОВ; место жительства-БРЯНСК; родился - 8.12.81.
    """
    label = "RESULT"
    query = concat_ws(
        "; ",
        func.substr(func.upper(Student.first_name), 1, 1) + "." + func.upper(Student.last_name),
        "место жительства-" + func.upper(Student.city),
        "родился - " + F_DATE + "."
    ).label(label)
    query = select([query, Student.birthdate]).where(not_null(*Student.c))

    result_proxy = db.session.execute(query).fetchall()
    result = []
    for raw_proxy in result_proxy:
        i = raw_proxy[0].index(";")
        result.append((raw_proxy[0][:i].upper() + raw_proxy[0][i:])
                      .replace(F_DATE, raw_proxy[1].strftime("%#d.%m.%y")))

    return pd.DataFrame({label: result})


def third() -> pd.DataFrame:
    """
    Составьте запрос для таблицы STUDENT таким образом, чтобы выходная
    таблица содержала всего один столбец в следующем виде:
    б.кузнецов; место жительства-брянск; родился: 8-дек-1981.
    """
    label = "RESULT"
    query = func.lower(concat_ws(
        "; ",
        func.substr(Student.first_name, 1, 1) + "." + Student.last_name,
        "место жительства-" + Student.city,
        "родился: " + F_DATE + "."
    )).label(label)
    query = select([query, Student.birthdate]).where(not_null(*Student.c))

    result_proxy = db.session.execute(query)
    result = [
        raw[0].replace(F_DATE, raw[1].strftime("%#d-%b-%Y")).lower()
        for raw in result_proxy
    ]
    return pd.DataFrame({label: result})


def fourth() -> pd.DataFrame:
    """
    Составьте запрос для таблицы STUDENT таким образом, чтобы выходная
    таблица содержала всего один столбец в следующем виде:
    Борис Кузнецов родился в 1981 году.
    """
    label = "RESULT"
    query = (
            as_string(func.upper(func.substr(Student.first_name, 1, 1))) +
            func.lower(func.substr(Student.first_name, 2)) +
            " " +
            func.upper(func.substr(Student.last_name, 1, 1)) +
            func.lower(func.substr(Student.last_name, 2)) +
            " родился в " +
            F_DATE +
            " году."
    ).label(label)
    query = select([query, Student.birthdate]).where(not_null(*Student.c))

    result_proxy = db.session.execute(query)
    result = [
        raw[0].replace(F_DATE, raw[1].strftime("%Y"))
        for raw in result_proxy
    ]
    return pd.DataFrame({label: result})


def fifth() -> pd.DataFrame:
    """
    Вывести фамилии, имена студентов и величину получаемых ими
    стипендий, при этом значения стипендий должны быть увеличены в 100 раз.
    """
    query = select([Student.last_name,
                    Student.first_name,
                    (Student.stipend * 100).label("stipend")]).where(not_null(*Student.c))

    result_proxy = db.session.execute(query)
    result = {k: [] for k in result_proxy.keys()}
    for raw in result_proxy:
        for k in raw.keys():
            result[k].append(raw[k])

    return pd.DataFrame(result)


def sixth() -> pd.DataFrame:
    """
    Тоже, что и в задаче 4, но только для студентов 1, 2 и 4-го курсов и таким
    образом, чтобы фамилии и имена были выведены прописными буквами.
    """
    label = "RESULT"
    query = (
            func.upper(Student.first_name) +
            " " +
            func.upper(Student.last_name) +
            " родился в " +
            F_DATE +
            " году."
    ).label(label)
    query = select([query, Student.birthdate]).where(and_(not_null(*Student.c), Student.course.in_([1, 2, 4])))

    result_proxy = db.session.execute(query)
    result = [
        raw[0].replace(F_DATE, raw[1].strftime("%Y"))
        for raw in result_proxy
    ]
    return pd.DataFrame({label: result})


def seventh() -> pd.DataFrame:
    """
    Составьте запрос для таблицы UNIVERSITY таким образом, чтобы
    выходная таблица содержала всего один столбец в следующем виде:
    Код-10; ВГУ-г.ВОРОНЕЖ; Рейтинг=296.
    """
    label = "RESULT"
    query = concat_ws(
        "; ",
        "Код-" + as_string(University.id),
        func.upper(University.name) + "-г." + func.upper(University.city),
        "Рейтинг=" + as_string(University.rating) + "."
    ).label(label)
    query = select([query]).where(not_null(*University.c))

    result_proxy = db.session.execute(query)
    result = []
    for raw_proxy in result_proxy:
        i = raw_proxy[0].index("-г.") + 3
        j = i + raw_proxy[0][i:].index(";")
        result.append(raw_proxy[0][:i] + raw_proxy[0][i:j].upper() + raw_proxy[0][j:])

    return pd.DataFrame({label: result})


def eighth() -> pd.DataFrame:
    """
    Тоже, что и в задаче 7, но значения рейтинга требуется округлить до
    первого знака (например , значение 382 округляется до 400).
    """
    label = "RESULT"
    query = concat_ws(
        "; ",
        "Код-" + as_string(University.id),
        func.upper(University.name) + "-г." + func.upper(University.city),
        "Рейтинг=" + F_DIGIT + "."
    ).label(label)
    query = select([query, University.rating]).where(not_null(*University.c))

    result_proxy = db.session.execute(query)
    result = [row[0].replace(F_DIGIT, str(round(row[1], -len(str(row[1])) + 1)))
              for row in result_proxy]
    return pd.DataFrame({label: result})


if __name__ == '__main__':
    answer(1, first())
    answer(2, second())
    answer(3, third())
    answer(4, fourth())
    answer(5, fifth())
    answer(6, sixth())
    answer(7, seventh())
    answer(8, eighth())
