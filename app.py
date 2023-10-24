from config import my_app
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    my_app.run(debug=True, host='localhost', port=8000)