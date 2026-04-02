import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_ltc_tw_2025_practitioner_resource_on_aa12():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'resourceType': 'Practitioner',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPractitioner'],
        'identifiers': [{
            'use': 'official',
            'system': 'https://www.tph.mohw.gov.tw',
            'value': 'DR001234'
        },
        {
            'use': 'official',
            'system': 'http://www.immigration.gov.tw',
            'value': 'A123456789'
        }],
        'name': [{
            'text': '王醫師',
            'family': '王',
            'given': ['志明'],
            'prefix': ['Dr.']
        }],
        'telecom': [{
            'system': 'phone',
            'value': '02-23123456',
            'use': 'work'
        },
        {
            'system': 'email',
            'value': 'dr.wang@hospital.tw',
            'use': 'work'
        }],
        'address': [{
            'text': '台北市中正區重慶南路一段122號',
            'line': ['重慶南路一段122號'],
            'city': '台北市',
            'district': '中正區',
            'postalCode': '100',
            'country': 'TW'
        }],
        'gender': 'male',
        'birth_date': '1975-06-15',
        'qualification': [{
            'identifier': [{
                'system': 'https://www.mohw.gov.tw',
                'value': 'MD123456'
            }],
            'code': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0360',
                    'code': 'MD',
                    'display': 'Doctor of Medicine'
                }]
            },
            'period': {
                'start': '2000-07-01'
            },
            'issuer': {
                'display': '台灣大學醫學院'
            }
        }]
    }

    with open('/app/app/tests/ltc_tw_2025/Practitioner-ltc-practitioner-physician-aa12-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    json_dict['type'] = 'aa12'
    response = client.post('/api/v1/ltc_tw_2025_practitioner', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['identifier']) == 2

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json

def test_create_ltc_tw_2025_practitioner_resource_on_ltc():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'resourceType': 'Practitioner',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPractitioner'],
        'identifiers': [{
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'MD'
                }]
            },
            'system': 'http://example.org/fhir/NamingSystem/hospital-license',
            'value': 'KMD12345'
        }],
        'active': True,
        'name': [{
            'use': 'official',
            'text': '王美玲',
            'family': '王',
            'given': ['美玲']
        }],
        'telecom': [{
            'system': 'phone',
            'value': '02-87654321',
            'use': 'work'
        },
        {
            'system': 'email',
            'value': 'meiling.wang@ltc-hospital.tw',
            'use': 'work'
        }],
        'address': [{
            'use': 'work',
            'type': 'both',
            'text': '台北市大安區復興南路二段201號',
            'line': ['復興南路二段201號'],
            'city': '台北市',
            'district': '大安區',
            'postalCode': '106',
            'country': 'TW'
        }],
        'gender': 'female',
        'birth_date': '1975-06-10'
    }

    with open('/app/app/tests/ltc_tw_2025/Practitioner-ltc-practitioner-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    json_dict['type'] = 'ltc'
    response = client.post('/api/v1/ltc_tw_2025_practitioner', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['identifier']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json

def test_create_ltc_tw_2025_practitioner_resource_on_nurse():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'resourceType': 'Practitioner',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCPractitioner'],
        'identifiers': [{
            'use': 'official',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'PRN',
                    'display': 'Provider Number'
                }]
            },
            'system': 'http://example.org/fhir/NamingSystem/practitioner-id',
            'value': 'N123456789'
        }],
        'active': True,
        'name': [{
            'use': 'official',
            'text': '王美玲',
            'family': '王',
            'given': ['美玲']
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
        'gender': 'female',
        'qualification': [{
            'identifier': [{
                'system': 'http://example.org/fhir/NamingSystem/nursing-license',
                'value': '護理執照123456'
            }],
            'code': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '224535009',
                    'display': 'Registered nurse'
                }]
            }
        }]
    }

    with open('/app/app/tests/ltc_tw_2025/Practitioner-ltc-practitioner-nurse-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    json_dict['type'] = 'nurse'
    response = client.post('/api/v1/ltc_tw_2025_practitioner', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['identifier']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json
