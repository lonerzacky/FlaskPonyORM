from connection import db, PrimaryKey, Required


class SysRmodul(db.Entity):
    _table_ = 'sys_rmodul'
    sysrole_kode = Required(str)
    sysmodul_kode = Required(str)
    PrimaryKey(sysrole_kode, sysmodul_kode)
