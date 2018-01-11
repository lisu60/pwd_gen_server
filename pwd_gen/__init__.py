from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pwd_gen.blueprints.api import api
from flask_bcrypt import Bcrypt

app = Flask(__name__, instance_relative_config=True)
print('instance path: %s' % app.instance_path)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.register_blueprint(api)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

