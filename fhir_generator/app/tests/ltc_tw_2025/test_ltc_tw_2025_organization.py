import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_ltc_tw_2025_organization_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'resourceType': 'Organization',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/Organization-twltc'],
        'identifiers': [{
            'use': 'usual',
            'type': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                    'code': 'PRN',
                    'display': 'Provider Number'
                }]
            },
            'system': 'http://www.moi.gov.tw',
            'value': '0131060029'
        }],
        'active': True,
        'types': [{
            'coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
                'code': 'prov',
                'display': 'Healthcare Provider'
            }]
        }],
        'name': '新北市私立安康老人長期照顧中心（養護型）',
        'telecom': [{
            'system': 'phone',
            'value': '02-29412345',
            'use': 'work'
        },
        {
            'system': 'fax',
            'value': '02-29412346',
            'use': 'work'
        }],
        'address': [{
            'use': 'work',
            'type': 'physical',
            'text': '新北市中和區安康路二段123號',
            'line': ['安康路二段123號'],
            'city': '中和區',
            'state': '新北市',
            'postalCode': '23511',
            'country': 'TW'
        }],
        'contact': [{
            'purpose': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/contactentity-type',
                    'code': 'ADMIN',
                    'display': 'Administrative'
                }]
            },
            'name': {
                'use': 'official',
                'family': '王',
                'given': ['志明']
            },
            'telecom': [{
                'system': 'phone',
                'value': '02-29412345',
                'use': 'work'
            }]
        }]
    }

    with open('/app/app/tests/ltc_tw_2025/Organization-ltc-organization-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    response = client.post('/api/v1/ltc_tw_2025_organization', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['identifier']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json
