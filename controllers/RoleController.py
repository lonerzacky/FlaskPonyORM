from flask import request
from flask_restful import Resource
from connection import select, db_session, commit
import utility
from models.sys_role import SysRole


# noinspection PyTypeChecker
class GetRole(Resource):
    @staticmethod
    def get():
        try:
            with db_session:
                data = select(row for row in SysRole)
                result = [row.to_dict() for row in data]
                return utility.give_response("00", "GET ROLE SUKSES", result)
        except Exception as e:
            return utility.give_response("01", str(e))


class InsertRole(Resource):
    @staticmethod
    def post():
        try:
            with db_session:
                sysrole_kode = request.form['sysrole_kode']
                sysrole_nama = request.form['sysrole_nama']
                c = SysRole(sysrole_kode=sysrole_kode, sysrole_nama=sysrole_nama)
                commit()
                return utility.give_response("00", "INSERT ROLE SUKSES", c.to_dict())
        except Exception as e:
            return utility.give_response("01", str(e))


class UpdateRole(Resource):
    @staticmethod
    def put(sysrole_kode):
        try:
            with db_session:
                sysrole_nama = request.form['sysrole_nama']
                sys_role = SysRole[sysrole_kode]
                sys_role.set(sysrole_nama=sysrole_nama)
                return utility.give_response("00", "UPDATE ROLE SUKSES", sys_role.to_dict())
        except Exception as e:
            return utility.give_response("01", str(e))


class DeleteRole(Resource):
    @staticmethod
    def delete(sysrole_kode):
        try:
            with db_session:
                SysRole[sysrole_kode].delete()
                return utility.give_response("00", "DELETE ROLE SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))
