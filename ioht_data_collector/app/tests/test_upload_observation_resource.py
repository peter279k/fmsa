import json
import httpx
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_upload_observation_resource_without_meta_profile_and_text():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with open('/app/app/tests/Organization-ltc-organization-example.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://fhir_data_manager:8000/api/v1/update/Organization', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('/app/app/tests/Patient-ltc-patient-chen-ming-hui.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://fhir_data_manager:8000/api/v1/update/Patient', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('/app/app/tests/Observation-ltc-observation-blood-pressure-example.json', 'r', encoding='utf-8') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {}
    payload['payload'] = json_dict

    response = client.post('/api/v1/observation_resource', headers=headers, json=payload)
    assert response.status_code == 201 or response.status_code == 200
    assert response.json()['message'] == ''
