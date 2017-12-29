from flask import Blueprint
from config import *

api = Blueprint('api', __name__, url_prefix=GLOBAL_PREFIX+'/api/v1.0')
from . import routes
