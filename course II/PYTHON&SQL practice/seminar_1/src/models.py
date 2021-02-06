from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text

CASCADE = "CASCADE"  # может где-то есть эти константы


@as_declarative()
class Base(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"
    id = Column(Integer, primary_key=True, autoincrement=True)


class Article(Base):
    """Статья на форуме"""
    title = Column(String(200), nullable=False, index=True)
    content = Column(Text(15000), nullable=False)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id", ondelete=CASCADE))

    def __repr__(self):
        return f'<{self.__class__.__name__} (' \
               f'title={self.title}, ' \
               f'content={self.content}, ' \
               f'date={self.date}' \
               f')>'

    __str__ = __repr__


class ArticleComment(Base):
    """Комментарий к статье"""
    text = Column(Text(2000), nullable=False)
    date = Column(DateTime)
    article_id = Column(Integer, ForeignKey("articles.id", ondelete=CASCADE))
    parent_id = Column(Integer, ForeignKey("articlecomments.id", ondelete=CASCADE))
    user_id = Column(Integer, ForeignKey("users.id", ondelete=CASCADE))

    def __repr__(self):
        return f'<{self.__class__.__name__} (' \
               f'text={self.text}, ' \
               f'date={self.date}' \
               f')>'

    __str__ = __repr__


class User(Base):
    """Пользователь форума"""
    username = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete=CASCADE))
    country = Column(String(200), nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__} (' \
               f'username={self.username}, ' \
               f'password={self.password}, ' \
               f'email={self.email}, ' \
               f'country={self.country}, ' \
               f'role_id={self.role_id}' \
               f')>'

    __str__ = __repr__


class Role(Base):
    """Роль пользователя"""
    name = Column(String(60), nullable=False, unique=True)

    def __repr__(self):
        return f'<{self.__class__.__name__} (' \
               f'name={self.name}' \
               f')>'

    __str__ = __repr__


if __name__ == '__main__':
    from database import DataBase
    db = DataBase()
    # Base.metadata.create_all(db.engine)
    # Base.metadata.drop_all(db.engine)
