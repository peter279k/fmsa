import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_track18_2024_practitioner_role_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/practitionerrole-iclaim'],
            'practitioner': {
                'reference': 'Practitioner/Practitioner-Chen',
                'display': '陳健骨'
            },
            'code': [{
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '405279007',
                    'display' : 'Attending physician (occupation)'
                }]
            }],
        },
    }

    with open('/app/app/tests/expected_track8_2024_practitioner_role.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_practitioner_role', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)
