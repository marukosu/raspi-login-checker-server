from flask import Flask
from .controllers import app as blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/raspi-login-checker?charset=utf8'
db = SQLAlchemy(app)