from flask import Response, Flask, jsonify
from config import my_app
from models.user_model import User
from app import app



@app.get('/users/v1')
def get_users():
    return_value = jsonify({'users': User.get_all_users()})
    return return_value

@app.get('/users/v1/{username}')
def get_by_username(username):
    response = Response(str(User.get_user(username)), 200, mimetype='application/json')
    return response