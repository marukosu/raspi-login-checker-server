from flask import Flask
from .controllers import app as blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('../config/default.py')
app.config.from_envvar('FLASK_CONFIG_FILE', silent=True)

app.register_blueprint(blueprint)

db = SQLAlchemy(app)

from .models import *