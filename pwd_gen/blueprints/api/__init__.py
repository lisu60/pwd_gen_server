from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/pwd_gen/api/v1.0')

from . import routes
