from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import (Column, Integer, String, DateTime, ForeignKey, CheckConstraint, Float)

__all__ = [
    "Client",
    "Bank",
    "Base"
]

CASCADE = "CASCADE"
SHORT_VARCHAR = 80


@as_declarative()
class Base(object):
    id = Column(Integer(), primary_key=True, autoincrement=True)

    @classmethod
    @property
    def columns(cls):
        return cls.__table__.columns

    c = columns

    def _repr(self, **args) -> str:
        field_strings = []
        for key, field in args.items():
            field_strings.append(f'{key}={field!r}')

        return f"<{self.__class__.__name__} {field_strings}>"

    @declared_attr
    def __tablename__(self):
        # TODO: split по uppercase

        return self.__name__.lower()

    def __repr__(self) -> str:
        return self._repr(id=self.id)

    __str__ = __repr__


class Client(Base):
    first_name = Column(String(SHORT_VARCHAR), nullable=False)
    last_name = Column(String(SHORT_VARCHAR), nullable=False)
    account_balance = Column(Integer, ForeignKey("bank.id", ondelete="SET NULL"))

    def __repr__(self):
        return self._repr(first_name=self.first_name,
                          last_name=self.last_name,
                          account_balance=self.account_balance)


class Bank(Base):
    name = Column(String(SHORT_VARCHAR), nullable=False)
    balance = Column(Float, default=0)

    def __repr__(self):
        return self._repr(name=self.name, balance=self.balance)
