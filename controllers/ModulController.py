import utility
from flask_jwt_extended import jwt_required
from flask import request
from flask_restful import Resource
from connection import db_session, commit
from models.sys_modul import SysModul


class GetModul(Resource):
    @staticmethod
    @jwt_required
    def get():
        try:
            with db_session:
                data = SysModul.select()
                result = [row.to_dict() for row in data]
                return utility.give_response("00", "GET MODUL SUKSES", result)
        except Exception as e:
            return utility.give_response("01", str(e))


class InsertModul(Resource):
    @staticmethod
    @jwt_required
    def post():
        try:
            with db_session:
                sysmodul_kode = request.form["sysmodul_kode"]
                sysmodul_nama = request.form["sysmodul_nama"]
                sysmodul_url = request.form["sysmodul_url"]
                sysmodul_icon = request.form["sysmodul_icon"]
                sysmodul_parent = request.form["sysmodul_parent"]
                sysmodul_no_urut = request.form["sysmodul_no_urut"]
                if not sysmodul_parent:
                    sysmodul_parent = None
                c = SysModul(sysmodul_kode=sysmodul_kode, sysmodul_nama=sysmodul_nama,
                             sysmodul_url=sysmodul_url, sysmodul_icon=sysmodul_icon,
                             sysmodul_parent=sysmodul_parent, sysmodul_no_urut=sysmodul_no_urut)
                commit()
                return utility.give_response("00", "INSERT MODUL SUKSES", c.to_dict())
        except Exception as e:
            return utility.give_response("01", str(e))


class UpdateModul(Resource):
    @staticmethod
    @jwt_required
    def put(sysmodul_kode):
        try:
            with db_session:
                sysmodul_nama = request.form["sysmodul_nama"]
                sysmodul_url = request.form["sysmodul_url"]
                sysmodul_icon = request.form["sysmodul_icon"]
                sysmodul_parent = request.form["sysmodul_parent"]
                if not sysmodul_parent:
                    sysmodul_parent = None
                sysmodul_no_urut = request.form["sysmodul_no_urut"]
                sys_modul = SysModul[sysmodul_kode]
                sys_modul.set(sysmodul_nama=sysmodul_nama, sysmodul_url=sysmodul_url,
                              sysmodul_icon=sysmodul_icon, sysmodul_parent=sysmodul_parent,
                              sysmodul_no_urut=sysmodul_no_urut)
                return utility.give_response("00", "UPDATE MODUL SUKSES", sys_modul.to_dict())
        except Exception as e:
            return utility.give_response("01", str(e))


class DeleteModul(Resource):
    @staticmethod
    @jwt_required
    def delete(sysmodul_kode):
        try:
            with db_session:
                SysModul[sysmodul_kode].delete()
                return utility.give_response("00", "DELETE MODUL SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))
