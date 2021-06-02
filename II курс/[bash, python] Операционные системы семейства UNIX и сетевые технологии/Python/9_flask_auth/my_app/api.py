from flask import Blueprint, abort, request
from flask_restful import Api, Resource
from peewee import DoesNotExist, IntegrityError

from my_app import sevices


class User(Resource):

    def get(self, user_id):
        try:
            return sevices.UserService.get_by_id(user_id), 200
        except DoesNotExist:
            abort(404)


class UserList(Resource):

    def get(self):
        try:
            return sevices.UserService.get_all(), 200
        except DoesNotExist:
            abort(404)


class SignUp(Resource):

    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        if password and username:
            try:
                return sevices.UserService.create(username, password), 201
            except IntegrityError:
                return {'message': 'Invalid data format'}, 400
        else:
            return {'message': 'Invalid data format'}, 400


api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(SignUp, '/auth/signUp')
