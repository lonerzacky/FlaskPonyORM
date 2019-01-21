from connection import db, Required, PrimaryKey, Optional


class SysModul(db.Entity):
    _table_ = 'sys_modul'
    sysmodul_kode = PrimaryKey(str)
    sysmodul_nama = Required(str)
    sysmodul_url = Required(str)
    sysmodul_icon = Required(str)
    sysmodul_parent = Optional(str, nullable=True)
    sysmodul_no_urut = Required(int)
