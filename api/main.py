from flask import Response, Flask, jsonify
from config import my_app
from models.user_model import User
from db_config import db



app = Flask(__name__)


@app.get('/dbsetup')
def create_db():
    db.drop_all()
    db.create_all()
    User.add_user_td()
    response_text = '{ "message": "Database created." }'
    response = Response(response_text, 200, mimetype='application/json')
    return response


@app.get('/')
def welcome():
    return {"message": "Hello, welcome to Johnny's Flask-API"}, 200


@app.get('/health')
def health():
    response_text = '{"status": "OK"}'
    response = Response(response_text, status=200, mimetype="application/json")
    return response