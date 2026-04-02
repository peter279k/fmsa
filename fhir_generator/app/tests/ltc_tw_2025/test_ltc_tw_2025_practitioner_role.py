import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_ltc_tw_2025_practitioner_role_resource_on_nurse():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'resourceType': 'PractitionerRole',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPractitionerRole'],
        'active': True,
        'practitioner': {
            'reference': 'Practitioner/ltc-practitioner-nurse-example'
        },
        'organization': {
            'reference': 'Organization/ltc-organization-example'
        },
        'code': [{
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '224535009',
                'display': 'Registered nurse'
            }]
        }],
        'specialty': [{
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '394609007',
                'display': 'General surgery (qualifier value)'
            }]
        }],
        'telecom': [{
            'system': 'phone',
            'value': '02-29412345',
            'use': 'work'
        },
        {
            'system': 'email',
            'value': 'meiling.wang@ltc-center.tw',
            'use': 'work'
        }],
        'available_time': [{
            'daysOfWeek': [
                'mon',
                'tue',
                'wed',
                'thu',
                'fri'
            ],
            'availableStartTime': '08:00:00',
            'availableEndTime': '17:00:00'
        }]
    }

    with open('/app/app/tests/ltc_tw_2025/PractitionerRole-ltc-practitioner-role-nurse-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    response = client.post('/api/v1/ltc_tw_2025_practitioner', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['availableTime']) == 1
    assert len(response_json['data'][0]['telecom']) == 2

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json
