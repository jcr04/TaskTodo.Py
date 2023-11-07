# config/config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/task'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
