from .core import app, db
from .models import *
from .controllers import app as blueprint

app.register_blueprint(blueprint)
