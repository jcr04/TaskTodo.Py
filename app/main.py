from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.models import task
db.create_all()