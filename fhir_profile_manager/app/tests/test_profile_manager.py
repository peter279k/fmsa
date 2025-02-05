import json
import pytest
import datetime
from app.main import app
from urllib.parse import urlencode
from fastapi.testclient import TestClient


client = TestClient(app)
created = ''
new_created = ''
inserted_id = ''
structure_definition_id = ''

def test_retrieve_profile_metadata_with_disallowed_params():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    params = {}
    encoded_uri = urlencode(params)
    response = client.get('/api/v1/profile?{}'.format(encoded_uri), headers=headers)

    expected_status_code = 400
    expected_message = 'Allowed params should be version,name,created'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1

def test_retrieve_profile_metadata_with_allowed_params():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    params = {'version': '1.0'}
    encoded_uri = urlencode(params)
    response = client.get('/api/v1/profile?{}'.format(encoded_uri), headers=headers)

    expected_status_code = 200
    expected_message = 'Retrieving specific Profile is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1

@pytest.mark.dependency()
def test_create_profile_metadata():
    created_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/StructureDefinition-observationbloodloss-imri.json', 'r') as f:
        structure_definition = f.read()

    payload = {
        'version': '0.1.0',
        'name': 'StructureDefinition-observationbloodloss-imri',
        'created': created_datetime,
        'structure_definition': structure_definition,
    }

    response = client.post('/api/v1/create_profile_metadata', headers=headers, json=payload)

    expected_status_code = 200
    expected_message = 'Creating specific Profile metadata is successful.'
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

@pytest.mark.dependency()
def test_upload_profile_with_creating_new_profile():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/StructureDefinition-observationbloodloss-imri.json', 'r') as f:
        structure_definition = f.read()

    json_profile_dict = json.loads(structure_definition)
    del json_profile_dict['id']
    payload = {
        'structure_definition': json.dumps(json_profile_dict),
    }

    response = client.post('/api/v1/upload_profile', headers=headers, json=payload)

    expected_created_status_code = 201
    expected_message = 'Uploading specific Profile is successful.'
    response_json = response.json()

    assert response.status_code == expected_created_status_code
    assert response_json['status'] == expected_created_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1

    global structure_definition_id
    structure_definition_id = response_json['data'][0]['result']['id']

@pytest.mark.dependency()
def test_update_profile_with_specific_profile_id():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/StructureDefinition-observationbloodloss-imri.json', 'r') as f:
        structure_definition = f.read()

    json_profile_dict = json.loads(structure_definition)
    payload = {
        'structure_definition': json.dumps(json_profile_dict),
    }

    response = client.put('/api/v1/update_profile', headers=headers, json=payload)

    expected_status_codes = [200, 201]
    expected_message = 'Updating specific Profile is successful.'
    response_json = response.json()

    assert response.status_code in expected_status_codes
    assert response_json['status'] in expected_status_codes
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1

@pytest.mark.dependency(depends=['test_upload_profile_with_creating_new_profile'])
def test_retrieve_profile_from_fhir_server_with_specific_id():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/StructureDefinition-observationbloodloss-imri.json', 'r') as f:
        structure_definition = f.read()

    json_profile_dict = json.loads(structure_definition)
    del json_profile_dict['id']

    response = client.get(f'/api/v1/retrieve_profile?_id={structure_definition_id}', headers=headers)

    expected_created_status_code = 200
    expected_message = 'Retrieving specific Profile is successful.'
    response_json = response.json()

    assert response.status_code == expected_created_status_code
    assert response_json['status'] == expected_created_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1
    assert response_json['data'][0]['result']['total'] == 1

@pytest.mark.dependency(depends=['test_update_profile_with_specific_profile_id'])
def test_retrieve_updated_profile_from_fhir_server_with_specific_id():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/StructureDefinition-observationbloodloss-imri.json', 'r') as f:
        structure_definition = f.read()

    json_profile_dict = json.loads(structure_definition)

    response = client.get(f'/api/v1/retrieve_profile?_id={json_profile_dict['id']}', headers=headers)

    expected_created_status_code = 200
    expected_message = 'Retrieving specific Profile is successful.'
    response_json = response.json()

    assert response.status_code == expected_created_status_code
    assert response_json['status'] == expected_created_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1
    assert response_json['data'][0]['result']['total'] == 1
    assert response_json['data'][0]['result']['entry'][0]['resource'] == json_profile_dict

@pytest.mark.dependency(depends=['test_create_profile_metadata'])
def test_retrieve_profile_metadata_with_one():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    params = {'version': '0.1.0', 'name': 'StructureDefinition-observationbloodloss-imri'}
    encoded_uri = urlencode(params)

    response = client.get('/api/v1/profile?{}'.format(encoded_uri), headers=headers)

    with open('/app/app/tests/StructureDefinition-observationbloodloss-imri.json', 'r') as f:
        expected_structure_definition = f.read()

    expected_status_code = 200
    expected_version = '0.1.0'
    expected_name = 'StructureDefinition-observationbloodloss-imri'
    expected_message = 'Retrieving specific Profile is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 1
    assert response_json['data'][0]['version'] == expected_version
    assert response_json['data'][0]['name'] == expected_name
    assert response_json['data'][0]['structure_definition'] == expected_structure_definition

@pytest.mark.dependency(depends=['test_create_profile_metadata'])
def test_update_profile_metadata():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with open('/app/app/tests/StructureDefinition-observationbloodloss-imri.json', 'r') as f:
        structure_definition = f.read()

    global new_created
    new_created = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    payload = {
        'version': '0.1.0',
        'name': 'StructureDefinition-observationbloodloss-imri',
        'created': created,
        'structure_definition': structure_definition,
        'new_version': '0.1.1',
        'new_name': 'StructureDefinition-observationbloodloss-imri',
        'new_created': new_created,
        'new_structure_definition': structure_definition,
    }
    response = client.put('/api/v1/update_profile_metadata', headers=headers, json=payload)

    expected_status_code = 200
    expected_message = 'Updating specific Profile metadata is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 2
    assert response_json['data'][1]['deleted_result'] >= 1
    assert response_json['data'][1]['inserted_result'] != inserted_id

@pytest.mark.dependency(depends=['test_update_profile_metadata'])
def test_delete_profile_metadata():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'version': '0.1.1',
        'name': 'StructureDefinition-observationbloodloss-imri',
        'created': new_created,
    }
    encoded_uri = urlencode(payload)
    response = client.delete(f'/api/v1/delete_profile_metadata?{encoded_uri}', headers=headers)

    expected_status_code = 200
    expected_message = 'Deleting specific Profile metadata is successful.'
    response_json = response.json()

    assert response.status_code == expected_status_code
    assert response_json['status'] == expected_status_code
    assert response_json['message'] == expected_message
    assert len(response_json['data']) == 2
    assert response_json['data'][1]['deleted_result'] == 1
