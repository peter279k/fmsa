import json
from app.main import app
from urllib.parse import urlencode
from fastapi.testclient import TestClient


client = TestClient(app)

def test_retrieve_ig_metadata_with_disallowed_params():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    params = {}
    encoded_uri = urlencode(params)
    response = client.get('/api/v1/ig?{}'.format(encoded_uri), headers=headers)

    expected_status_code = 400
    expected_message = 'Allowed params should be version,name,created'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1

def test_retrieve_ig_metadata_with_allowed_params():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    params = {'version': '1.0'}
    encoded_uri = urlencode(params)
    response = client.get('/api/v1/ig?{}'.format(encoded_uri), headers=headers)

    expected_status_code = 200
    expected_message = 'Retrieving specific Implementation Guide is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1
