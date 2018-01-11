from . import db


class BaseModel(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timpstamp())