import json
import connexion
import pytest
import os

from config import my_app
from db_config import db 

flask_app = connexion.FlaskApp(__name__)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(my_app.root_path, 'database/test.db')
flask_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
flask_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(flask_app.app)  
flask_app.add_api('../swagger.yml')


@pytest.fixture(scope='module')
def client():
    with flask_app.app.test_client() as c:
        yield c


# @pytest.fixture(scope='module')
def helper(json_info):
    for info in json_info:
        first_row = info.decode("utf-8")
        return str(json.loads(first_row))


def test_0001_get(client):
    td_username = 'thor'

    response = client.get(f'/users/v1/{td_username}')
    

    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 200
