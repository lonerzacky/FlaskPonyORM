from connection import db, Required, PrimaryKey
from passlib.hash import pbkdf2_sha256 as sha256


class Jwt(db.Entity):
    _table_ = 'jwt'
    id = PrimaryKey(int, auto=True)
    username = Required(str)
    password = Required(str)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hashed):
        return sha256.verify(password, hashed)
