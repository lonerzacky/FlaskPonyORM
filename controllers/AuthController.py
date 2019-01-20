from flask import request
from flask_restful import Resource
from models.sys_user import SysUser
from connection import db_session, select
import queryUtils
import utility


# noinspection PyTypeChecker
class VerifyLogin(Resource):
    @staticmethod
    def post():
        try:
            with db_session:
                sysuser_nama = request.form["sysuser_nama"]
                sysuser_passw = utility.create_hash(request.form["sysuser_passw"])
                count = select(
                    c for c in SysUser if c.sysuser_nama == sysuser_nama and c.sysuser_passw == sysuser_passw).count()
                result_row = queryUtils.get_info_user(sysuser_nama, sysuser_passw)
                if count == 1:
                    return utility.give_response("00", "LOGIN SUKSES", result_row)
                else:
                    return utility.give_response("01", "LOGIN GAGAL")
        except Exception as e:
            return utility.give_response("01", str(e))
