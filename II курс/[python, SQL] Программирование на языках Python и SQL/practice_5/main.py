from sqlalchemy import select, cast, text, VARCHAR
from sqlalchemy.sql import func, functions

from src.database import DataBase
from src.models import *

db = DataBase()

q = select([func.upper(cast(Student.last_name, VARCHAR))])
print(db.session.execute(q).fetchall())
