from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="../static", template_folder="../production")
app.config.from_object('config')

db = SQLAlchemy(app)
Bootstrap(app)

from app import views, models
