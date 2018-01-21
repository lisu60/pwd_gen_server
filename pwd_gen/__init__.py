from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pwd_gen.blueprints.api import api
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from . import models

app = Flask(__name__, instance_relative_config=True)
print('instance path: %s' % app.instance_path)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.register_blueprint(api)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'

@login_manager.user_loader
def load_user(uid):
    return models.User.User.query.filter(models.User.User.id == uid).first()


