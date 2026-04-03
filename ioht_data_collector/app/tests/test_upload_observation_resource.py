import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_upload_observation_resource_without_meta_profile_and_text():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with open('/app/app/tests/Observation-ltc-observation-blood-pressure-example.json', 'r', encoding='utf-8') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {}
    payload['payload'] = json_dict

    response = client.post('/api/v1/observation_resource', headers=headers, json=payload)
    assert response.status_code == 201
    assert response.json()['status'] == 201
    assert response.json()['message'] == ''
