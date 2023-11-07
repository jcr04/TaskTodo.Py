from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.models.task import Task
db.create_all()

from app.routes.task_routes import init_app
init_app(app)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
