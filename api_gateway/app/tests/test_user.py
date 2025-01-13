import pytest
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_get_fsma_version():
    response = client.get('/api/v1/')

    assert response.status_code == 200
    assert response.json()['message'] == 'v1'

@pytest.mark.dependency()
def test_initial_config_register_user():
    initial_response = client.get('/api/v1/initial', headers={'Accept': 'application/json'})
    initial_response_json = initial_response.json()
    assert initial_response.status_code == 200
    assert initial_response_json['status'] == 200
    assert initial_response_json['message'] == 'FMSA configuration is sucessful.'

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'username': 'test',
        'password': 'test123',
        'first_name': 'Test',
        'last_name': 'Li',
        'email': 'test@email.com',
    }
    response = client.post('/api/v1/register', headers=headers, json=data)

    assert response.status_code == 200
    assert len(response.json()['data']) == 1

@pytest.mark.dependency(depends=['test_initial_config_register_user'])
def test_duplicated_register_user():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'username': 'test_duplicated',
        'password': 'test123',
        'first_name': 'Test',
        'last_name': 'Li',
        'email': 'test@email.com',
    }
    response = client.post('/api/v1/register', headers=headers, json=data)

    assert response.status_code == 200

    duplicated_response = client.post('/api/v1/register', headers=headers, json=data)
    duplicated_json_response = duplicated_response.json()

    assert duplicated_response.status_code == 200
    assert len(duplicated_json_response['data']) > 0
    assert duplicated_json_response['status'] == 409

@pytest.mark.dependency(depends=['test_initial_config_register_user'])
def test_user_login():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'username': 'test',
        'password': 'test123',
    }

    response = client.post('/api/v1/login', headers=headers, json=data)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json['data'][0].get('access_token') is not None

def test_x_user_header_is_missed():
    response = client.get('/api/v1/generate_care_plan')

    assert response.status_code == 400
    assert response.json()['detail'] == 'The x-user is missing in headers!'

def test_x_api_key_header_is_missed():
    headers = {'x-user': 'user'}
    response = client.get('/api/v1/generate_care_plan', headers=headers)

    assert response.status_code == 401
    assert response.json()['detail'] == 'You didn\'t pass the api key in the header! Header: x-api-key'

def test_x_api_key_header_is_invalid():
    headers = {'x-user': 'user', 'x-api-key': '12345'}
    response = client.get('/api/v1/generate_care_plan', headers=headers)

    assert response.status_code == 401
    assert response.json()['detail'] == 'You pass the x-user is not found in the header!'
