from .BaseModel import BaseModel
from .. import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin


class User(BaseModel, UserMixin):
    email = db.Column(db.VARCHAR(100), nullable=False, unique=True)
    _password = db.Column(db.VARCHAR(128), nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        if bcrypt.check_password_hash(self._password, plaintext):
            return True

        return False
