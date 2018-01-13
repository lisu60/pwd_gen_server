from .BaseModel import BaseModel
from .. import db
from sqlalchemy.dialects.mysql import TINYINT


class Site(BaseModel):

    uid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.VARCHAR(100), nullable=True)
    site = db.Column(db.VARCHAR(200), nullable=False)
    month_key = db.Column(db.VARCHAR(100), nullable=False)
    length_min = db.Column(db.Integer, nullable=False)
    length_max = db.Column(db.Integer, nullable=True)
    char_specs = db.Column(TINYINT, nullable=False)