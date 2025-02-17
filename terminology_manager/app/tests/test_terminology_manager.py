import os
import json
import pytest
import datetime
import subprocess
from app.main import app
from urllib.parse import urlencode
from fastapi.testclient import TestClient


client = TestClient(app)
created = ''
new_created = ''
inserted_id = ''
processed_id = ''

def test_retrieve_terminology_metadata_with_disallowed_params():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    params = {}
    encoded_uri = urlencode(params)
    response = client.get('/api/v1/terminology?{}'.format(encoded_uri), headers=headers)

    expected_status_code = 400
    expected_message = 'Allowed params should be version,name,created,filename'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1

def test_retrieve_terminology_metadata_with_allowed_params():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    params = {'version': '1.0'}
    encoded_uri = urlencode(params)
    response = client.get('/api/v1/terminology?{}'.format(encoded_uri), headers=headers)

    expected_status_code = 200
    expected_message = 'Retrieving specific Terminology is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1

@pytest.mark.dependency()
def test_create_terminology_metadata():
    created_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'version': '2.72',
        'name': 'loinc',
        'created': created_datetime,
        'filename': 'Loinc_2.72.zip',
    }

    response = client.post('/api/v1/create_terminology_metadata', headers=headers, json=payload)

    expected_status_code = 200
    expected_message = 'Creating specific Terminology metadata is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 2
    assert response_json['data'][0] == payload
    assert type(response_json['data'][1]['inserted_id']) is str

    global created, inserted_id
    inserted_id = response_json['data'][1]['inserted_id']
    created = created_datetime

@pytest.mark.dependency(depends=['test_create_terminology_metadata'])
def test_retrieve_terminology_metadata_with_one():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    params = {'version': '2.72', 'name': 'loinc'}
    encoded_uri = urlencode(params)

    response = client.get('/api/v1/terminology?{}'.format(encoded_uri), headers=headers)

    expected_status_code = 200
    expected_version = '2.72'
    expected_name = 'loinc'
    expected_filename = 'Loinc_2.72.zip'
    expected_message = 'Retrieving specific Terminology is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1
    assert response_json['data'][0]['version'] == expected_version
    assert response_json['data'][0]['name'] == expected_name
    assert response_json['data'][0]['filename'] == expected_filename

def test_upload_terminology():
    files = {
        'zip_file': open('/app/app/tests/Loinc_2.72.zip', 'rb'),
    }
    response = client.post('/api/v1/upload_terminology', files=files)

    expected_status_code = 200
    expected_message = 'Uploading specific Terminology is successful.'
    expected_filesize = 87061668
    expected_filename = 'Loinc_2.72.zip'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1
    assert response_json['data'][0]['filesize'] == expected_filesize
    assert response_json['data'][0]['filename'] == expected_filename
    assert os.path.isfile('/tmp/Loinc_2.72.zip') is True

@pytest.mark.dependency(depends=['test_create_terminology_metadata'])
def test_update_terminology_metadata():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    global new_created
    new_created = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    payload = {
        'version': '2.72',
        'name': 'loinc',
        'created': created,
        'filename': 'Loinc_2.72.zip',
        'new_version': '2.73',
        'new_name': 'loinc',
        'new_created': new_created,
        'new_filename': 'Loinc_2.73.zip',
    }
    response = client.put('/api/v1/update_terminology_metadata', headers=headers, json=payload)

    expected_status_code = 200
    expected_message = 'Updating specific Terminology metadata is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 2
    assert response_json['data'][1]['deleted_result'] >= 1
    assert response_json['data'][1]['inserted_result'] != inserted_id
    assert os.path.isfile('/tmp/Loinc_2.72.zip') is False

@pytest.mark.dependency(depends=['test_update_terminology_metadata'])
def test_delete_terminology_metadata():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'version': '2.73',
        'name': 'loinc',
        'created': new_created,
        'filename': 'Loinc_2.73.zip',
    }
    encoded_uri = urlencode(payload)
    response = client.delete(f'/api/v1/delete_terminology_metadata?{encoded_uri}', headers=headers)

    expected_status_code = 200
    expected_message = 'Deleting specific Terminology metadata is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 2
    assert response_json['data'][1]['deleted_result'] == 1

@pytest.mark.dependency()
def test_retrieve_archived_code_system():
    subprocess.run(['cp', '/app/app/tests/Loinc_2.72.zip', '/tmp/'])

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    encoded_uri = urlencode({'filename': 'Loinc_2.72.zip'})

    response = client.get(f'/api/v1/retrieve_archived_code_system?{encoded_uri}', headers=headers)

    expected_status_code = 200
    expected_content_size = 87061668

    assert response.status_code == expected_status_code
    assert len(response.content) == expected_content_size

def test_call_importing_archived_code_system_with_non_existed_file():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    encoded_uri = urlencode({'filename': 'non_existed.zip'})

    response = client.get(f'/api/v1/call_importing_archived_code_system?{encoded_uri}', headers=headers)

    expected_status_code = 400

    assert response.status_code == expected_status_code
    assert response.json()['message'] == 'The /tmp/non_existed.zip file is not found.'

@pytest.mark.dependency(depends=['test_retrieve_archived_code_system'])
def test_call_importing_archived_code_system_with_existed_file():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    encoded_uri = urlencode({'filename': 'Loinc_2.72.zip'})

    response = client.get(f'/api/v1/call_importing_archived_code_system?{encoded_uri}', headers=headers)
    response_json = response.json()

    expected_status_code = 200

    assert response.status_code == expected_status_code
    assert response_json['message'] == 'Importing the Loinc_2.72.zip is on the way.'

    global processed_id
    processed_id = response_json['data'][0]['processed_id']

@pytest.mark.dependency(depends=['test_call_importing_archived_code_system_with_existed_file'])
def test_call_retrieving_code_system_log():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    encoded_uri = urlencode({'processed_id': processed_id})

    response = client.get(f'/api/v1/call_retrieving_code_system_log?{encoded_uri}', headers=headers)

    expected_status_code = 200

    assert response.status_code == expected_status_code
    assert response.json()['message'] == 'Retrieve code system importing log is successful'

def test_create_code_system():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with open('/app/app/tests/pa_tempcode.json', 'r') as f:
        pa_temp_code_json_str = f.read()

    pa_temp_code_json = json.loads(pa_temp_code_json_str)
    response = client.put(f'/api/v1/create_code_system', headers=headers, json=pa_temp_code_json)

    expected_status_code = 200

    assert response.status_code == expected_status_code
    assert response.json()['id'] == 'tempcode'
