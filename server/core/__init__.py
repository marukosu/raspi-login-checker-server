from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_pyfile('../../config/default.py')
app.config.from_envvar('FLASK_CONFIG_FILE')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

