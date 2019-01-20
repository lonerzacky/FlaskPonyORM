from flask_restful import Resource
from connection import db_session

import utility
from models.sys_user import SysUser


class GetUser(Resource):
    @staticmethod
    def get():
        try:
            with db_session:
                    data = SysUser.select()
                    result = [row.to_dict() for row in data]
                    return utility.give_response("00", "GET USER SUKSES", result)
        except Exception as e:
            return utility.give_response("01", str(e))
