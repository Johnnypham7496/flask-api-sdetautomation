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


def test_tc0001_get(client):
    td_username = 'darth'

    response = client.get('/users/v1')
    json_info = helper(response.response)
    

    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 200
    
    if td_username not in json_info:
        print(f'FAIL: Not able to find td{td_username}')
        assert False


def test_tc0002_get_by_username(client):
    td_username = 'thor'

    response = client.get(f'/users/v1/{td_username}')
    json_info = helper(response.response)
    

    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 200
    
    if td_username not in json_info:
        print(f'FAIL: Not able to find td{td_username}')
        assert False


def test_tc0003_post(client):
    td_username = 'batman'
    td_email = 'batman@gmail.com'

    response = client.post('/users/v1', data = json.dumps(dict(
        username= td_username,
        email= td_email
    )), mimetype='application/json')
    json_info = helper(response.response)

    assert response.status_code == 201

    if td_username not in json_info and td_email not in json_info:
        print(f'FAIL: Not able to find td{td_username}')
        assert False

    # this codes deletes the data from the test.db after creating to ensure our post fucntion always passes wihtout committed the changes to the test.db
    client.delete(f'/users/v1/{td_username}')


def test_tc0004_users_put(client):
    td_username = 'darth'
    td_email = 'luke@gmail.com'

    response = client.put(f'/users/v1/{td_username}', data= json.dumps(dict(
        email= td_email
    )), mimetype='application/json')

    assert response.status_code == 204

    response = client.get(f'/users/v1/{td_username}')
    json_info = helper(response.response)

    assert response.status_code == 200

    if td_email not in json_info:
        print(f'FAIL: Not able to find td{td_email}')
        assert False


def test_tc0005_delete(client):
    td_username = 'delete'
    td_email = 'test@example.com'

    response = client.post('/users/v1', data = json.dumps(dict(
        username= td_username,
        email= td_email
    )), mimetype='application/json')

    assert response.status_code == 201

    delete_response = client.delete(f'/users/v1/{td_username}')

    assert delete_response.status_code == 204


def test_tc0006_bad_post(client):
    td_username = 'et'
    td_email = 'et@gmail.com'
    td_error_message = '{\'error\': "\'username\' is a required property."}'

    response = client.post('/users/v1', data= json.dumps(dict(
        user= td_username,
        email= td_email
    )), mimetype='application/json')

    assert response.status_code == 400

    json_info = str(helper(response.response))

    if td_error_message not in json_info:
        print(f'FAIL: Error message not found {td_error_message}')
        assert False


def test_tc0007_bad_put(client):
    td_username = 'darth'
    td_email = 'luke@gmail.com'
    td_error_message = '{\'error\': "\'email\' is a required property."}'

    response = client.put(f'/users/v1/{td_username}', data= json.dumps(dict(
        mail= td_email
    )), mimetype='application/json')

    assert response.status_code == 400

    json_info = helper(response.response)

    if td_error_message not in json_info:
        print(f'FAIL: Error message not found {td_error_message}')
        assert False