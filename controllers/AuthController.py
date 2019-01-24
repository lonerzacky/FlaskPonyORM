import queryUtils
import utility
from flask_jwt_extended import jwt_required
from flask import request
from flask_restful import Resource
from models.sys_user import SysUser
from connection import db_session, select, commit


# noinspection PyTypeChecker
class VerifyLogin(Resource):
    @staticmethod
    @jwt_required
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


class ChangePassword(Resource):
    @staticmethod
    @jwt_required
    def post():
        try:
            with db_session:
                sysuser_id = request.form["sysuser_id"]
                old_password_from_data = queryUtils.get_old_password(sysuser_id)
                password_lama = utility.create_hash(request.form["password_lama"])
                password_baru = utility.create_hash(request.form["password_baru"])
                if password_lama == old_password_from_data:
                    sys_user = SysUser[sysuser_id]
                    sys_user.set(sysuser_passw=password_baru)
                    commit()
                    return utility.give_response("00", "UBAH PASSWORD SUKSES")
                else:
                    return utility.give_response("01", "PASSWORD LAMA TIDAK SAMA")
        except Exception as e:
            return utility.give_response("01", str(e))
