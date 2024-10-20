import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Local SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
