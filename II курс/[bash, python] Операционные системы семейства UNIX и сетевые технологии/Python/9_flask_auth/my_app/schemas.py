from flask_marshmallow import Marshmallow

from my_app import app

ma = Marshmallow(app)


class UserSchema(ma.Schema):
    class Meta:
        fields = ['username', 'password', 'created_at']


user = UserSchema()
users = UserSchema(many=True)
