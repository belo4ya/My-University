import time

from sqlalchemy.exc import SQLAlchemyError

from src.db import DataBase
from src.models import *

db = DataBase


def select_all_banks():
    print(db.session.query(Bank).all())


def send_amount(amount: float, from_: Client, to_: Client):
    from_.balance -= amount
    select_all_banks()

    start = time.time()
    time.sleep(5)
    if time.time() - start > 4:
        raise TimeoutError("Банк клиента не может получить деньги")

    to_.balance += amount


select_all_banks()

try:
    with db.session.begin():
        me = db.session.query(Bank).join(Client).filter_by(first_name="Alexey", last_name="Kovalev").first()
        other = db.session.query(Bank).join(Client).filter_by(last_name="Чичиков").first()
        me.balance += 2_000

        select_all_banks()

        send_amount(1_000, me, other)
except (SQLAlchemyError, TimeoutError) as e:
    print(e)
    db.session.rollback()
    db.session.close()

select_all_banks()
