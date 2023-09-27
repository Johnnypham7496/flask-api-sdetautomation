from config import my_app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(my_app.app)