from my_app import models
from my_app import schemas
from passlib.hash import pbkdf2_sha256 as sha256


class UserService:

    @staticmethod
    def get_by_id(pk):
        user = models.User.get_by_id(pk)
        return schemas.user.dump(user)

    @staticmethod
    def get_all():
        users = models.User.select().execute()
        return schemas.users.dump(users)

    @classmethod
    def create(cls, username, password):
        user = models.User.create(username=username, password=cls.hash_password(password))
        return schemas.user.dump(user)

    @classmethod
    def hash_password(cls, password):
        return sha256.hash(password)

    @classmethod
    def verify_password(cls, password, hash):
        return sha256.verify(password, hash)
