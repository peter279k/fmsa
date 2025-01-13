import os
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

def test_x_api_key_header_is_invalid_or_expired():
    headers = {'x-user': 'user', 'x-api-key': '12345'}
    response = client.get('/api/v1/generate_care_plan', headers=headers)

    assert response.status_code == 401
    assert response.json()['detail'] == 'You pass the invalid or expired api key in the header!'

def test_x_api_key_header_is_expired():
    expired_token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ4N1BQcXEtUUl5dHUwSWt4ZU5DazZpRGtrN1RnM05ZaUd6YjRkdXBleEl3In0.eyJleHAiOjE3MzY3NzY2NTgsImlhdCI6MTczNjc3NjM1OCwianRpIjoiZWY0OGUzZTAtMGU4Ni00YTg0LTljYmYtYmM5MGE1OGJlMGVkIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9mbXNhIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImI0NzcwZDg1LTljZDItNDkzZi1hYWJiLTkxNmY2YTdmMGI4ZSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImZtc2EiLCJzZXNzaW9uX3N0YXRlIjoiMzQyZjEwYjUtNmY5MC00NjM5LWE4NzAtMWQwNmMyYjNhY2ZhIiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJkZWZhdWx0LXJvbGVzLWZtc2EiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCBwcm9maWxlIiwic2lkIjoiMzQyZjEwYjUtNmY5MC00NjM5LWE4NzAtMWQwNmMyYjNhY2ZhIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoiVGVzdCBMaSIsInByZWZlcnJlZF91c2VybmFtZSI6InRlc3QiLCJnaXZlbl9uYW1lIjoiVGVzdCIsImZhbWlseV9uYW1lIjoiTGkiLCJlbWFpbCI6InRlc3RAZW1haWwuY29tIn0.pV2bXezZg---M8zr82DDo_49ET-BdTojvuLpbe5QHcG94DUuHIrJyNd7ibphSOUZyplourrKNWQwEaGUs7POyTRayW0pVytHdS5muZifFJhJ7HImyQ5_1XA4TAZyLKr1RsPdYzgvu_urj7Vii0FdiC0TXvPhayfpUIj9V1i_KPboDLmUDMrcAjsNnHl3VCT-ECiu6uPrOwmZGCN3YHn8lo7s85DeeSqeYlzs7nO2yDSbj89wep612A-hPuzlke9glT8nj6YvOT92b-UDXKAVKn2VP3qkv8fT-1SjZPaielsck6kWD1KtTicOPwblyyHZF8o8S_-J1Va_Eq1W7d2q2g'
    headers = {
        'x-user': 'user',
        'x-api-key': expired_token,
    }
    response = client.get('/api/v1/generate_care_plan', headers=headers)

    assert response.status_code == 401
    assert response.json()['detail'] == 'You pass the invalid or expired api key in the header!'
