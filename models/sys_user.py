from connection import db, Required, PrimaryKey


class SysUser(db.Entity):
    _table_ = 'sys_user'
    sysuser_id = PrimaryKey(int)
    sysrole_kode = Required(str)
    sysuser_nama = Required(str)
    sysuser_passw = Required(str)
    sysuser_namalengkap = Required(str)
    sysuser_email = Required(str)


db.generate_mapping(create_tables=True)
