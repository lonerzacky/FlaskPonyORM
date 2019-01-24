import utility
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required)
from connection import db_session, commit, select, delete
from models.jwt import Jwt

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


# noinspection PyTypeChecker
class UserRegistration(Resource):
    @staticmethod
    def post():
        data = parser.parse_args()
        try:
            with db_session:
                username = data['username']
                password = Jwt.generate_hash(data['password'])
                find_exist = select(c for c in Jwt if c.username == username).count()
                if find_exist == 1:
                    return utility.give_response("01", "User Exist", username)
                else:
                    Jwt(username=username, password=password)
                    commit()
                    access_token = create_access_token(identity=data['username'])
                    refresh_token = create_refresh_token(identity=data['username'])
                    data_jwt = {
                        'message': 'User {} was created'.format(data['username']),
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }
                    return utility.give_response("00", data_jwt)
        except Exception as e:
            return utility.give_response("01", str(e))


# noinspection PyTypeChecker
class UserLogin(Resource):
    @staticmethod
    def post():
        data = parser.parse_args()
        try:
            with db_session:
                username = data["username"]
                password = data["password"]
                data_user = Jwt.get(username=username)
                if Jwt.verify_hash(password, data_user.password):
                    access_token = create_access_token(identity=data['username'])
                    refresh_token = create_refresh_token(identity=data['username'])
                    data_jwt = {
                        'message': 'Logged in as {}'.format(data_user.username),
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }
                    return utility.give_response("00", data_jwt)
                else:
                    return utility.give_response("01", "Wrong credentials")
        except Exception as e:
            return utility.give_response("01", str(e))


class UserLogoutAccess(Resource):
    @staticmethod
    def post():
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    @staticmethod
    def post():
        return {'message': 'User logout'}


class TokenRefresh(Resource):
    @staticmethod
    def post():
        return {'message': 'Token refresh'}


# noinspection PyTypeChecker
class AllUsers(Resource):
    @staticmethod
    def get():
        try:
            with db_session:
                data = Jwt.select()
                result = [row.to_dict() for row in data]
                return utility.give_response("00", "List Of Users", result)
        except Exception as e:
            return utility.give_response("01", str(e))

    @staticmethod
    def delete():
        try:
            with db_session:
                delete(row for row in Jwt)
                return utility.give_response("00", "Deleted All Users")
        except Exception as e:
            return utility.give_response("01", str(e))


class SecretResource(Resource):
    @staticmethod
    @jwt_required
    def get():
        return dict(answer=42)
