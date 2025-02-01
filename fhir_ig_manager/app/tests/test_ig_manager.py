import os
import pytest
import datetime
from app.main import app
from urllib.parse import urlencode
from fastapi.testclient import TestClient


client = TestClient(app)
inserted_id = ''

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

@pytest.mark.dependency()
def test_create_ig_metadata():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'version': '0.1.0',
        'name': 'imri',
        'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'filename': 'full-ig-imri-0.1.0.zip',
    }

    response = client.post('/api/v1/create_ig_metadata', headers=headers, json=payload)

    expected_status_code = 200
    expected_message = 'Creating specific Implementation Guide metadata is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 2
    assert response_json['data'][0] == payload
    assert type(response_json['data'][1]['inserted_id']) is str

    global inserted_id
    inserted_id = response_json['data'][1]['inserted_id']

@pytest.mark.dependency(depends=['test_create_ig_metadata'])
def test_retrieve_ig_metadata_with_one():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    params = {'version': '0.1.0', 'name': 'imri'}
    encoded_uri = urlencode(params)

    response = client.get('/api/v1/ig?{}'.format(encoded_uri), headers=headers)

    expected_status_code = 200
    expected_version = '0.1.0'
    expected_name = 'imri'
    expected_filename = 'full-ig-imri-0.1.0.zip'
    expected_message = 'Retrieving specific Implementation Guide is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1
    assert response_json['data'][0]['version'] == expected_version
    assert response_json['data'][0]['name'] == expected_name
    assert response_json['data'][0]['filename'] == expected_filename

def test_upload_ig():
    files = {
        'zip_file': open('/app/app/tests/full-ig-imri-0.1.0.zip', 'rb'),
    }
    response = client.post('/api/v1/upload_ig', files=files)

    expected_status_code = 200
    expected_message = 'Uploading specific Implementation Guide is successful.'
    expected_filesize = 36565636
    expected_filename = 'full-ig-imri-0.1.0.zip'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1
    assert response_json['data'][0]['filesize'] == expected_filesize
    assert response_json['data'][0]['filename'] == expected_filename
    assert os.path.isfile('/tmp/full-ig-imri-0.1.0.zip') is True

@pytest.mark.dependency(depends=['test_create_ig_metadata'])
def test_update_ig_metadata():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'doc_id': inserted_id,
        'new_version': '0.1.1',
        'new_name': 'imri',
        'new_created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'new_filename': 'full-ig-imri-0.1.1.zip',
    }
    response = client.put('/api/v1/update_ig_metadata', headers=headers, json=payload)

    expected_status_code = 200
    expected_message = 'Updating specific Implementation Guide metadata is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 2
    assert response_json['data'][1]['deleted_result'] == 1
    assert response_json['data'][1]['inserted_result'] == 1
