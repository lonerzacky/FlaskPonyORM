from connection import db, Required, PrimaryKey


class Sys_role(db.Entity):
    _table_ = 'sys_role'
    sysrole_kode = PrimaryKey(str)
    sysrole_nama = Required(str)


db.generate_mapping(create_tables=True)
