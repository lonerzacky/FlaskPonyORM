from flask_restful import Resource, reqparse

import utility
from connection import db_session, commit, select, delete, db
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
                    c = Jwt(username=username, password=password)
                    commit()
                    return utility.give_response("00", "User Created", c.to_dict())
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
                if Jwt.verify_hash(password,
                                   '$pbkdf2-sha256$29000$IGRMSekdI8QYYwxh7J3Tmg$TtJEYh23BO7dVScJFG.vpMyL4f2l7SfYfa34dmzIbio'):
                    return utility.give_response("00", 'Logged in as {}'.format(data["username"]), data)
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
    def get():
        return {
            'answer': 42
        }
