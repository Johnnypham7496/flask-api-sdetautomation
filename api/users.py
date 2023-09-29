from flask import Response, Flask, jsonify, request, json
from config import my_app
from models.user_model import User
from messages.error_messages import invalid_post_msg_users
from validations.validation import validate_user_object, validate_put_request_object
from app import app



@app.get('/users/v1')
def get_users():
    return_value = jsonify({'users': User.get_all_users()})
    return return_value

@app.get('/users/v1/{username}')
def get_by_username(username):
    response = Response(str(User.get_user(username)), 200, mimetype='application/json')
    return response


@app.post('/users/v1/')
def add_user():
    request_data = request.get_json()
    if validate_user_object(request_data):
        User.add_user(request_data['username'], request_data['email'])
        response = Response(json.dumps(request_data), 201, mimetype='application/json')
        response.headers['Location'] = '/users/v1' + str(request_data['username'])
    else:
        response = Response(json.dumps(invalid_post_msg_users), 400, mimetype='application/json') 
    return response 