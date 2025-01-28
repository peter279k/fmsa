import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_track8_2024_practitioner_role_resource():
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

def test_create_track8_2024_practitioner_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/practitioner-iclaim'],
            'identifiers': [{
                'use': 'official',
                'type': {
                    'coding': [{
                        'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code' : 'MD'
                    }]
                },
                'system' : 'https://www.cgh.org.tw',
                'value' : '031932'
            }],
            'name': [{
                'use': 'official',
                'text': '陳健骨'
            }]
        },
    }

    with open('/app/app/tests/expected_track8_2024_practitioner.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_practitioner', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_patient_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/patient-iclaim'],
            'extension': [{
                'url': 'https://claim.cgh.org.tw/iclaim/StructureDefinition/cathay-occupation',
                'valueCodeableConcept': {
                    'coding': [{
                        'system': 'https://claim.cgh.org.tw/iclaim/CodeSystem/lia-roc-occupation-values',
                        'code': '00010010'
                    }]
                }
            }],
            'identifiers': [{
                'use' : 'official',
                'type' : {
                    'coding' : [{
                        'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code' : 'NNxxx',
                        '_code' : {
                            'extension' : [{
                                'extension' : [{
                                    'url' : 'suffix',
                                    'valueString' : 'TWN'
                                },
                                {
                                    'url' : 'valueSet',
                                    'valueCanonical' : 'http://hl7.org/fhir/ValueSet/iso3166-1-3'
                                }],
                                'url' : 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/identifier-suffix'
                            }]
                        }
                    }]
                },
                'system' : 'http://www.moi.gov.tw',
                'value' : 'C251401029'
            },
            {
                'use' : 'official',
                'type' : {
                    'coding' : [{
                        'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code' : 'MR'
                    }]
                },
                'system' : 'https://www.cgh.org.tw',
                'value' : 'ADCM9487'
            }],
            'name_use': 'usual',
            'name_text': '郝美麗',
            'gender': 'female',
            'birth_date' : '1990-04-22',
            'address': [{
                'extension' : [{
                    'url' : 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-number',
                    'valueString' : '365號'
                }],
                'text' : '台北市北投區明德路365號',
                'line' : ['明德路'],
                'city' : '北投區',
                'district' : '台北市',
                'country' : 'TW'
            }]
        },
    }

    with open('/app/app/tests/expected_track8_2024_patient.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_patient', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_organization_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/organization-hosp-imri'],
            'identifiers': [{
                'use': 'official',
                'type': {
                    'coding': [{
                        'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code': 'PRN'
                    }]
                },
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/organization-identifier-tw',
                'value': '1101020018'
            }],
            'type_coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
                'code': 'prov'
            }],
            'name': '國泰醫療財團法人國泰綜合醫院',
        },
    }

    with open('/app/app/tests/expected_track8_2024_organization_min.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_organization', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)
