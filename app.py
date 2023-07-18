from flask import Response, Flask, jsonify


app = Flask(__name__)


@app.get('/')
def hello_world():
    return {"message": "Hello World"}, 200


@app.get('/health')
def health():
    response_text = '{"status": "OK"}'
    response = Response(response_text, status=200, mimetype="application/json")
    return response


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)