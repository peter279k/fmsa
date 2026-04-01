import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_ltc_tw_2025_patient_resource_on_ltc_type():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'resourceType': 'Patient',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPatient'],
        'identifiers': [{
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'PRN',
                    'display': 'Provider Number'
                }]
            },
            'system': 'http://www.ankang-ltc.tw',
            'value': 'R2024001'
        },
        {
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'NNxxx',
                    'display': 'National Person Identifier where the xxx is the ISO table 3166 3-character (alphabetic) country code'
                }],
                'text': 'National Person Identifier (TWN)'
            },
            'system': 'http://www.moi.gov.tw',
            'value': 'A123456789'
        }],
        'active': True,
        'names': [{
            'use': 'official',
            'text': 'Chen Ming Hui'
        },
        {
            'use': 'usual',
            'text': '陳明慧'
        }],
        'telecom': [{
            'system': 'phone',
            'value': '0912345678',
            'use': 'mobile'
        }],
        'gender': 'female',
        'birth_date': '1945-03-15',
        'address': [{
            'use': 'home',
            'text': '新北市中和區安康路二段123號3樓301室',
            'line': ['安康路二段123號3樓301室'],
            'city': '中和區',
            'state': '新北市',
            'postalCode': '23511',
            'country': 'TW'
        },
        {
            'use': 'billing',
            'text': '台北市大安區和平東路二段76號2樓',
            'line': ['和平東路二段76號2樓'],
            'city': '大安區',
            'state': '台北市',
            'postalCode': '10663',
            'country': 'TW'
        }],
        'contact': [{
            'relationship': [{
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0131',
                    'code': 'N',
                    'display': 'Next-of-Kin'
                }]
            }],
            'name': {
                'use': 'usual',
                'text': '陳志強'
            },
            'telecom': [{
                'system': 'phone',
                'value': '0987654321',
                'use': 'mobile'
            },
            {
                'system': 'phone',
                'value': '02-27031234',
                'use': 'home'
            }]
        }],
        'managing_organization': {
            'reference': 'Organization/ltc-organization-example'
        }
    }

    with open('/app/app/tests/ltc_tw_2025/Patient-ltc-patient-chen-ming-hui.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    json_dict['type'] = 'ltc'
    response = client.post('/api/v1/ltc_tw_2025_patient', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['identifier']) == 2

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json

def test_create_ltc_tw_2025_patient_resource_on_cs100():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'resourceType': 'Patient',
        'identifiers': [{
            'system': 'https://example.org/mrn',
            'value': 'A0001'
        }],
        'names': [{
            'text': '王小明'
        }]
    }

    with open('/app/app/tests/ltc_tw_2025/Patient-ltc-patient-cs100-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    json_dict['type'] = 'cs100'
    response = client.post('/api/v1/ltc_tw_2025_patient', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['identifier']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json
