from connection import db, Required


class Logservice(db.Entity):
    _table_ = 'logservice'
    uri = Required(str)
    method = Required(str)
    params = Required(str)
    ip_address = Required(str)
    request_time = Required(str)
    response = Required(str, 65535)
    status = Required(str)
