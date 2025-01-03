import os
from .main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_get_fsma_version():
    response = client.get('/api/v1/')

    assert response.status_code == 200
    assert response.json()['message'] == 'v1'

def test_register_user():
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
