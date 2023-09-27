from flask import Response, Flask, jsonify
from config import my_app
from models.user_model import *



app = Flask(__name__)


def create_db():
    db.create_all()
    User.addd_user_td()
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


if __name__ == '__main__':
    my_app.run(debug=True, host='localhost', port=8000)