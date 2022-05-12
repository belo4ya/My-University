from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from models import Base, Role, User
from utils import SingletonMeta
import pprint

DATABASE = "sqlite"
DB_NAME = "forum.db"


class DataBase(metaclass=SingletonMeta):

    def __init__(self):
        self.engine = create_engine(f"{DATABASE}:///{DB_NAME}")
        self.session = sessionmaker(bind=self.engine)()

    def _create_all_tables(self):
        Base.metadata.create_all(self.engine)

    def _remove_all_tables(self):
        Base.metadata.drop_all(self.engine)

    def init_base_roles(self):
        super_user = Role(name="super")
        creator = Role(name="creator")
        default = Role(name="default")
        self.session.add(super_user)
        self.session.add(creator)
        self.session.add(default)
        self.session.commit()

    def create_user(self, username: str, password: str, email: str, country: str, role_id=None):
        user = User(username=username, password=password, email=email, country=country, role_id=role_id)
        self.session.add(user)
        self.session.commit()

    def show_all_users(self):
        users = self.session.query(User).all()
        pprint.pprint(users)

    def show_all_roles(self):
        roles = self.session.query(Role).all()
        pprint.pprint(roles)
