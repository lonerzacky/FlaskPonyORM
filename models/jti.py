from connection import db, Required, PrimaryKey, db_session


# noinspection PyTypeChecker,SqlDialectInspection,SqlNoDataSourceInspection
class Jti(db.Entity):
    _table_ = 'revoked_tokens'
    id = PrimaryKey(int, auto=True)
    jti = Required(str)

    @classmethod
    def is_jti_blacklisted(cls, jti):
        with db_session:
            data = db.execute("SELECT * FROM revoked_tokens WHERE jti=$jti",
                              globals={'jti': jti})
            result = data.fetchone()
            return bool(result)
