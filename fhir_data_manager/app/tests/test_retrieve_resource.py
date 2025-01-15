import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_retrieve_patient_resource_without_query_params():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.get('/api/v1/retrieve/Patient', headers=headers)

    assert response.status_code == 200
    assert response.json()['message'] == 'Retrieving Patient is successful.'

def test_retrieve_patient_resource_not_found_with_query_params():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.get('/api/v1/retrieve/Patient?_id=not_found', headers=headers)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json['message'] == 'Retrieving Patient is successful.'
    assert response_json['data'][0]['total'] == 0
