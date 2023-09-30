import json
import connexion
import pytest

from config import my_app

flask_app = connexion.FlaskApp(__name__)
flask_app.add_api('../swagger.yml')


@pytest.fixture(scope='module')
def client():
    with flask_app.app.test_client() as c:
        yield c


@pytest.fixture(scope='module')
def helper(json_info):
    for info in json_info:
        first_row = info.decode("utf-8")
        return str(json.loads(first_row))


    # Tests that the 'message' value is 'Hello, welcome to Johnny's Flask-API'
def test_tc0001_welcome(client):
    td_message = 'Hello, welcome to Johnny\'s Flask-API'

    response = client.get('/')
    
    assert response.status_code == 200
    assert response.get_json()['message'] == td_message


def test_tc0002_health(client):
    td_message = 'OK'

    response = client.get('/health')
    
    assert response.status_code == 200
    assert response.get_json()['status'] == td_message