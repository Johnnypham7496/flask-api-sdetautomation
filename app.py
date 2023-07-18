from flask import Response, Flask


app = Flask(__name__)


@app.get('/')
def hello_world():
    return {"message": "Hello World"}, 200 