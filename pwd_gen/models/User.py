from .BaseModel import BaseModel
from . import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

class User(BaseModel):
    email = db.Column(db.VARCHAR(100), nullable=False);
    _password = db.Column(db.VARCHAR(128))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)