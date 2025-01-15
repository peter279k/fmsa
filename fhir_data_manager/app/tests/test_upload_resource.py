import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_upload_patient_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/expected_track13_2024_patient.json', 'r', encoding='utf-8') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']

    payload = {}
    payload['resource'] = json_dict

    response = client.post('/api/v1/upload/Patient', headers=headers, json=payload)
    assert response.status_code == 201
    assert response.json()['message'] == 'Uploading Patient is successful.'
