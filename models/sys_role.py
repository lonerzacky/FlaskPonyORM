from connection import db, Required, PrimaryKey


class SysRole(db.Entity):
    _table_ = 'sys_role'
    sysrole_kode = PrimaryKey(str)
    sysrole_nama = Required(str)
