from flask_jwt_extended import jwt_required

import utility
from flask import request
from flask_restful import Resource
from connection import db_session, db, commit
from models.sys_user import SysUser


# noinspection SqlDialectInspection,SqlNoDataSourceInspection
class GetUser(Resource):
    @staticmethod
    @jwt_required
    def get():
        try:
            with db_session:
                data = db.execute("SELECT sysuser_id,sys_role.sysrole_kode,sys_role.sysrole_nama,"
                                  "sysuser_nama,sysuser_namalengkap,sysuser_email FROM sys_user "
                                  "INNER JOIN sys_role ON sys_user.sysrole_kode = sys_role.sysrole_kode")
                result = [dict((data.description[i][0], value)
                               for i, value in enumerate(row)) for row in data]
                return utility.give_response("00", "GET USER SUKSES", result)
        except Exception as e:
            return utility.give_response("01", str(e))


class InsertUser(Resource):
    @staticmethod
    @jwt_required
    def post():
        try:
            with db_session:
                sysuser_id = request.form["sysuser_id"]
                sysrole_kode = request.form["sysrole_kode"]
                sysuser_nama = request.form["sysuser_nama"]
                sysuser_passw = utility.create_hash(request.form["sysuser_passw"])
                sysuser_namalengkap = request.form["sysuser_namalengkap"]
                sysuser_email = request.form["sysuser_email"]
                c = SysUser(sysuser_id=sysuser_id, sysrole_kode=sysrole_kode, sysuser_nama=sysuser_nama,
                            sysuser_passw=sysuser_passw, sysuser_namalengkap=sysuser_namalengkap,
                            sysuser_email=sysuser_email)
                commit()
                return utility.give_response("00", "INSERT USER SUKSES", c.to_dict())

        except Exception as e:
            return utility.give_response("01", str(e))


class UpdateUser(Resource):
    @staticmethod
    @jwt_required
    def put(sysuser_id):
        try:
            with db_session:
                sysrole_kode = request.form["sysrole_kode"]
                sysuser_nama = request.form["sysuser_nama"]
                sysuser_namalengkap = request.form["sysuser_namalengkap"]
                sysuser_email = request.form["sysuser_email"]
                sys_user = SysUser[sysuser_id]
                sys_user.set(sysrole_kode=sysrole_kode, sysuser_nama=sysuser_nama,
                             sysuser_namalengkap=sysuser_namalengkap, sysuser_email=sysuser_email)
                return utility.give_response("00", "UPDATE USER SUKSES", sys_user.to_dict())
        except Exception as e:
            return utility.give_response("01", str(e))


class DeleteUser(Resource):
    @staticmethod
    @jwt_required
    def delete(sysuser_id):
        try:
            with db_session:
                SysUser[sysuser_id].delete()
                return utility.give_response("00", "DELETE USER SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))
