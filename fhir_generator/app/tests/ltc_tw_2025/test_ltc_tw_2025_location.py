import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_ltc_tw_2025_location_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'resourceType': 'Location',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/Location-twltc'],
        'status': 'active',
        'name': '新北市私立安康老人長期照顧中心（養護型）',
        'description': '失智症個案陳明輝目前所在的日照中心',
        'mode': 'instance',
        'types': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode',
                'code': 'PTRES',
                'display': 'Patient\'s Residence',
            }]
        }],
        'address': {
            'use': 'work',
            'type': 'physical',
            'text': '新北市中和區安康路二段123號'
        },
        'position': {
            'longitude': 121.5089,
            'latitude': 24.9936,
            'altitude': 25.5
        }
    }

    with open('/app/app/tests/ltc_tw_2025/Location-ltc-location-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    response = client.post('/api/v1/ltc_tw_2025_location', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['types']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json
