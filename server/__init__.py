from flask import Flask
from .controllers import app as blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)