from flask import Response, Flask, jsonify
from config import my_app


app = Flask(__name__)


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