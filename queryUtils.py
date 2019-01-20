from connection import db


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
