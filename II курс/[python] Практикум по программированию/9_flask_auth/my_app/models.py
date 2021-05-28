import datetime

from flask_peewee.auth import BaseUser
from peewee import *
from flask_peewee.db import Database

from my_app import app

db = Database(app)


class BaseModel(db.Model):
    id = PrimaryKeyField(null=False)


class User(BaseModel, BaseUser):
    username = CharField(unique=True, null=False)
    password = CharField(null=False)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = 'users'

    def __str__(self):
        return self.username
