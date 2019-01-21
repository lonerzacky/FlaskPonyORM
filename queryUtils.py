import datetime
import json
from flask import request
from connection import db, commit, db_session
from models.logservice import Logservice


# noinspection SqlResolve,SqlDialectInspection,SqlNoDataSourceInspection
def get_info_user(sysuser_nama, sysuser_passw):
    data = db.execute("SELECT sysuser_id,sys_role.sysrole_kode,sys_role.sysrole_nama,"
                      "sysuser_nama,sysuser_namalengkap,sysuser_email FROM sys_user "
                      "INNER JOIN sys_role ON sys_user.sysrole_kode = sys_role.sysrole_kode "
                      "WHERE sysuser_nama=$sysuser_nama AND sysuser_passw=$sysuser_passw",
                      globals={'sysuser_nama': sysuser_nama, 'sysuser_passw': sysuser_passw})
    result = [dict((data.description[i][0], value)
                   for i, value in enumerate(row)) for row in data.fetchall()]
    return result


# noinspection SqlResolve,SqlDialectInspection,SqlNoDataSourceInspection
def get_old_password(sysuser_id):
    data = db.execute("SELECT sysuser_passw FROM sys_user WHERE sysuser_id=$sysuser_id",
                      globals={'sysuser_id': sysuser_id})
    result = data.fetchone()
    return result[0]


def create_log(response, status):
    now = datetime.datetime.now()
    request_time = now.strftime("%Y-%m-%d %H:%M")
    if not request.form:
        request_form = json.dumps("none")
    else:
        request_form = json.dumps(request.form)
    with db_session:
        Logservice(uri=request.base_url, method=request.method, params=request_form,
                   ip_address=request.remote_addr, request_time=request_time,
                   response=response, status=status)
        commit()
