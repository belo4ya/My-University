import pprint
from datetime import datetime

from sqlalchemy import func

from src.database import DataBase
from src.models import *


def task(n):
    def wrapper(function):
        def decorator(*args, **kwargs):
            print(f"\n\n{n}. {function.__doc__.strip()}\n")
            return function(*args, **kwargs)
        return decorator
    return wrapper


@task(1)
def first_task(created=True):
    """
    Создать одного пользователя, для него один заказ,
    и в этом заказе детализировать два объекта в Амстердаме
    на майские праздники с 1 по 11 мая.
    """
    if not created:
        user = User(id=0, username='alexey', email='alex@mail.ru', phone='+79998887766', password='1234')
        order = Order(id=0, user=user)

        start_date = datetime(2021, 5, 1)
        end_date = datetime(2021, 5, 11)
        listings = DataBase.session.query(Listing)
        first_item = LineItem(id=0,
                              start_date=start_date,
                              end_date=end_date,
                              order=order,
                              listing=listings.get(5))
        second_item = LineItem(id=1,
                               start_date=start_date,
                               end_date=end_date,
                               order=order,
                               listing=listings.get(9))

        DataBase.session.add_all([user, order, first_item, second_item])
        DataBase.session.commit()
    pprint.pprint(DataBase.session.query(User, Order, LineItem).join(LineItem).join(User).filter(User.id == 0).all())


@task(2)
def second_task():
    """
    Распечатать число объектов в каждом районе.
    """
    pprint.pprint(DataBase.session.query(Neighbourhood.id, Neighbourhood.name, func.count()).join(Listing).group_by(
        Listing.neighbourhood_id).all())


@task(3)
def third_task():
    """
    Найти минимальную и максимальную цены объекта в каждом районе.
    """
    pprint.pprint(DataBase.session.query(Neighbourhood.id, Neighbourhood.name, func.max(Listing.price),
                                         func.min(Listing.price)).join(Listing).group_by(
        Listing.neighbourhood_id).all())


@task(4)
def fourth_task():
    """
    Найти все объекты в районе Osdorp с ценой выше средней по этому району.
    """
    neighbourhood_id = DataBase.session.query(Neighbourhood.id).filter_by(name='Osdorp')
    mean_price_by_neighbourhood = DataBase.session.query(
        func.avg(Listing.price)
    ).filter_by(neighbourhood_id=neighbourhood_id)

    pprint.pprint(DataBase.session.query(Listing).filter(
        Listing.neighbourhood_id == neighbourhood_id, Listing.price > mean_price_by_neighbourhood
    ).all())


if __name__ == '__main__':
    first_task()
    second_task()
    third_task()
    fourth_task()
