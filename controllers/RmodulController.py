from flask import request
from flask_restful import Resource
from connection import db_session, commit

import utility
from models.sys_rmodul import SysRmodul


class GetRmodul(Resource):
    @staticmethod
    def get():
        try:
            with db_session:
                data = SysRmodul.select()
                result = [row.to_dict() for row in data]
                return utility.give_response("00", "GET ROLE MODUL SUKSES", result)
        except Exception as e:
            return utility.give_response("01", str(e))


class InsertRModul(Resource):
    @staticmethod
    def post():
        try:
            with db_session:
                sysrole_kode = request.form["sysrole_kode"]
                sysmodul_kode = request.form["sysmodul_kode"]
                c = SysRmodul(sysrole_kode=sysrole_kode, sysmodul_kode=sysmodul_kode)
                commit()
                return utility.give_response("00", "INSERT ROLE MODUL SUKSES", c.to_dict())
        except Exception as e:
            return utility.give_response("01", str(e))


class DeleteRModul(Resource):
    @staticmethod
    def post():
        try:
            with db_session:
                sysrole_kode = request.form["sysrole_kode"]
                sysmodul_kode = request.form["sysmodul_kode"]
                SysRmodul[sysrole_kode, sysmodul_kode].delete()
                return utility.give_response("00", "DELETE ROLE MODUL SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))
