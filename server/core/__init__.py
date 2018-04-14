from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('../config/default.py')
app.config.from_envvar('FLASK_CONFIG_FILE')
db = SQLAlchemy(app)