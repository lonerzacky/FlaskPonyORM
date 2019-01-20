from flask_restful import Resource
from connection import db_session

import utility


class GetUser(Resource):
    @staticmethod
    def get():
        try:
            with db_session:
                data = ""
        except Exception as e:
            return utility.give_response("01", str(e))
