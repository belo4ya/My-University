from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, BigInteger, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relation

from datetime import datetime

__all__ = [
    'Base',
    'Listing',
    'User',
    'Order',
    'LineItem',
    'Host',
    'Neighbourhood',
    'RoomType',
    'PropertyType',
]

CASCADE = "CASCADE"
SHORT_VARCHAR = 80
MIDDLE_VARCHAR = 255


@as_declarative()
class Base:
    __repr_attrs__ = ['id']
    id = Column(BigInteger, primary_key=True, autoincrement=True)

    @declared_attr
    def __tablename__(self):
        table_name = ''
        ascii_upper = range(ord('A'), ord('Z') + 1)
        for i, s in enumerate(self.__name__):
            if ord(s) in ascii_upper and i != 0:
                table_name += '_'
            table_name += s.upper()

        return table_name + 'S'

    def __repr__(self):
        field_strings = []
        for attr in self.__repr_attrs__:
            field_strings.append(f'{attr}={getattr(self, attr)}')

        return f"<{self.__class__.__name__} {field_strings}>"

    __str__ = __repr__


class Listing(Base):
    name = Column(String(SHORT_VARCHAR), index=True, nullable=False)
    url = Column(String(SHORT_VARCHAR))
    amenities = Column(String(MIDDLE_VARCHAR))
    bedrooms = Column(Integer)
    beds = Column(Integer)
    price = Column(Float)

    host_id = Column(BigInteger, ForeignKey('HOSTS.id'))
    host = relation('Host')

    neighbourhood_id = Column(BigInteger, ForeignKey('NEIGHBOURHOODS.id'))
    neighbourhood = relation('Neighbourhood')

    property_type_id = Column(BigInteger, ForeignKey('PROPERTY_TYPES.id'))
    property_type = relation('PropertyType')

    room_type_id = Column(BigInteger, ForeignKey('ROOM_TYPES.id'))
    room_type = relation('RoomType')

    __repr_attrs__ = ['name', 'url']


class User(Base):
    username = Column(String(SHORT_VARCHAR), nullable=False, unique=True)
    email = Column(String(MIDDLE_VARCHAR), nullable=False)
    phone = Column(String(SHORT_VARCHAR), nullable=False)
    password = Column(String(SHORT_VARCHAR), nullable=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    __repr_attrs__ = ['username']


class Order(Base):
    created_on = Column(DateTime, default=datetime.now)

    user_id = Column(BigInteger, ForeignKey('USERS.id'))
    user = relation('User')


class LineItem(Base):
    start_date = Column(DateTime, nullable=False, default=datetime.now)
    end_date = Column(DateTime, nullable=False)

    order_id = Column(BigInteger, ForeignKey('ORDERS.id'))
    order = relation('Order')

    listing_id = Column(BigInteger, ForeignKey('LISTINGS.id'))
    listing = relation('Listing')

    __repr_attrs__ = ['start_date', 'end_date', 'listing']


class Host(Base):
    name = Column(String(SHORT_VARCHAR), nullable=False)


class Neighbourhood(Base):
    name = Column(String(SHORT_VARCHAR), nullable=False, unique=True)


class RoomType(Base):
    name = Column(String(SHORT_VARCHAR), nullable=False)


class PropertyType(Base):
    name = Column(String(SHORT_VARCHAR), nullable=False)
