import json
import httpx
import pytest


@pytest.mark.dependency()
def test_upload_required_references():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with open('/app/app/tests/scenarios/Practitioner-ltc-practitioner-physician-aa12-example.json')as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://fhir_data_manager:8000/api/v1/update/Practitioner', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200


    with open('/app/app/tests/scenarios/Practitioner-ltc-practitioner-nurse-example.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://fhir_data_manager:8000/api/v1/update/Practitioner', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('/app/app/tests/scenarios/PractitionerRole-ltc-practitioner-role-nurse-example.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://fhir_data_manager:8000/api/v1/update/PractitionerRole', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('/app/app/tests/scenarios/Organization-ltc-organization-example.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://fhir_data_manager:8000/api/v1/update/Organization', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('/app/app/tests/scenarios/Patient-ltc-patient-chen-ming-hui.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://fhir_data_manager:8000/api/v1/update/Patient', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('/app/app/tests/scenarios/Practitioner-ltc-practitioner-example.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://fhir_data_manager:8000/api/v1/update/Practitioner', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('/app/app/tests/scenarios/Location-ltc-location-example.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://fhir_data_manager:8000/api/v1/update/Location', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

@pytest.mark.dependency(depends=['test_upload_required_references'])
def test_closed_state_convert_upload_retrieve_observation_scenario1():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': 'API Key',
        'x-user': 'User',
    }
    payload = {
        'resourceType': 'Observation',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCObservationVitalSigns'],
        'status': 'final',
        'category_coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
            'code': 'vital-signs',
            'display': 'Vital Signs'
        }],
        'code_coding': [{
            'system': 'http://loinc.org',
            'code': '85354-9',
            'display': 'Blood pressure panel with all children optional'
        }],
        'code_text': '血壓',
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effective_datetime': '2024-01-15T09:00:00+08:00',
        'performer': [{
            'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
        }],
        'component': [{
            'code': {
                'coding': [{
                    'system': 'http://loinc.org',
                    'code': '8480-6',
                    'display': 'Systolic blood pressure'
                }]
            },
            'valueQuantity': {
                'value': 135,
                'unit': 'mmHg',
                'system': 'http://unitsofmeasure.org',
                'code': 'mm[Hg]'
            }
        },
        {
            'code': {
                'coding': [{
                    'system': 'http://loinc.org',
                    'code': '8462-4',
                    'display': 'Diastolic blood pressure'
                }]
            },
            'valueQuantity': {
                'value': 85,
                'unit': 'mmHg',
                'system': 'http://unitsofmeasure.org',
                'code': 'mm[Hg]'
            }
        }]
    }

    with open('/app/app/tests/scenarios/Observation-ltc-observation-blood-pressure-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    response = httpx.post('http://api_gateway:8000/api/v1/ltc_tw_2025_observation_blood_pressure', headers=headers, json=json_dict)

    response_json = response.json()
    observation_id = response_json['data'][0]['id']
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['category']) == 1
    assert len(response_json['data'][0]['code']['coding']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json

    response = httpx.get(f'http://api_gateway:8000/api/v1/retrieve/Observation?_id={observation_id}', headers=headers)

    assert response.status_code == 200

@pytest.mark.dependency(depends=['test_closed_state_convert_upload_retrieve_observation_scenario1'])
def test_half_open_state_convert_upload_retrieve_observation_scenario1():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': 'API Key',
        'x-user': 'User',
    }

    with open('/app/app/tests/scenarios/Observation-ltc-observation-blood-pressure-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    empty_payload = {}

    json_dict = {}
    json_dict['payload'] = empty_payload

    for _ in range(6):
        response = httpx.post('http://api_gateway:8000/api/v1/ltc_tw_2025_observation_blood_pressure', headers=headers, json=json_dict)

        assert response.status_code == 500


    payload = {
        'resourceType': 'Observation',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCObservationVitalSigns'],
        'status': 'final',
        'category_coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
            'code': 'vital-signs',
            'display': 'Vital Signs'
        }],
        'code_coding': [{
            'system': 'http://loinc.org',
            'code': '85354-9',
            'display': 'Blood pressure panel with all children optional'
        }],
        'code_text': '血壓',
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effective_datetime': '2024-01-15T09:00:00+08:00',
        'performer': [{
            'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
        }],
        'component': [{
            'code': {
                'coding': [{
                    'system': 'http://loinc.org',
                    'code': '8480-6',
                    'display': 'Systolic blood pressure'
                }]
            },
            'valueQuantity': {
                'value': 135,
                'unit': 'mmHg',
                'system': 'http://unitsofmeasure.org',
                'code': 'mm[Hg]'
            }
        },
        {
            'code': {
                'coding': [{
                    'system': 'http://loinc.org',
                    'code': '8462-4',
                    'display': 'Diastolic blood pressure'
                }]
            },
            'valueQuantity': {
                'value': 85,
                'unit': 'mmHg',
                'system': 'http://unitsofmeasure.org',
                'code': 'mm[Hg]'
            }
        }]
    }

    json_dict['payload'] = payload

    response = httpx.post('http://api_gateway:8000/api/v1/ltc_tw_2025_observation_blood_pressure', headers=headers, json=json_dict)

    assert response.status_code == 200
