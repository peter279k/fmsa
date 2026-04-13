import json
import httpx
import pytest
import hashlib
import secrets
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

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
def test_convert_upload_retrieve_observation_scenario1():
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
    response = client.post('/api/v1/ltc_tw_2025_observation_blood_pressure', headers=headers, json=json_dict)

    response_json = response.json()
    observation_id = response_json['data'][0]['id']
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['category']) == 1
    assert len(response_json['data'][0]['code']['coding']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json

    response = client.get(f'/api/v1/retrieve/Observation?_id={observation_id}', headers=headers)

    assert response.status_code == 200

@pytest.mark.dependency(depends=['test_upload_required_references'])
def test_convert_upload_retrieve_procedure_scenario2():
    with open('/app/app/tests/scenarios/procedure.json') as f:
        procedure_data = f.read()

    module_name = 'ProcedureLtcConverter'
    payload = {
        'module_name': module_name,
        'original_data': json.loads(procedure_data),
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': 'API Key',
        'x-user': 'User',
    }

    response = client.post(f'/api/v1/convert', headers=headers, json=payload)
    response_json = response.json()
    response_json_data = response_json['data'][0]

    assert response.status_code == 200

    assert response_json_data[0]['performedDateTime'] == '2025-03-01T08:00+08:00'
    assert response_json_data[-1]['performedDateTime'] == '2025-03-05T19:00+08:00'

    assert response_json_data[0]['code'] == {
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '225964003',
            'display': 'Assisting with personal hygiene'
        }],
        'text': '個人衛生協助',
    }
    assert response_json_data[-1]['code'] == {
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '225964003',
            'display': 'Assisting with personal hygiene'
        }],
        'text': '個人衛生協助',
    }

    assert response_json_data[0]['note'] == [{
        'time': '2025-03-01T08:00+08:00',
        'text': '合作度佳，情緒穩定',
    }]
    assert response_json_data[-1]['note'] == [{
        'time': '2025-03-05T19:00+08:00',
        'text': '情緒平靜，表示願意休息',
    }]

    procedure_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
    response_json_data[0]['id'] = procedure_id
    payload = {
        'resource': response_json_data[0],
    }
    response = client.put(f'/api/v1/update/Procedure', headers=headers, json=payload)

    assert response.status_code == 201

    response = client.get(f'/api/v1/retrieve/Procedure?_id={procedure_id}', headers=headers)

    assert response.status_code == 200

@pytest.mark.dependency(depends=['test_upload_required_references'])
def test_convert_upload_retrieve_medication_administration_data():
    with open('/app/app/tests/scenarios/medication_administration.json') as f:
        medication_admin_data = f.read()

    medication_lists = json.loads(medication_admin_data)['用藥紀錄']
    module_name = 'MedicationAdministrationLtcConverter'
    payload = {
        'module_name': module_name,
        'original_data': medication_lists,
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': 'API Key',
        'x-user': 'User',
    }

    response = client.post(f'/api/v1/convert', headers=headers, json=payload)
    response_json = response.json()
    response_json_data = response_json['data'][0]

    assert response.status_code == 200

    assert response_json_data[0]['effectiveDateTime'] == '2025-03-01T00:00+08:00'
    assert response_json_data[-1]['effectiveDateTime'] == '2022-12-01T00:00+08:00'

    assert response_json_data[0]['dosage'] == {
        'route': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '26643006',
                'display': 'Oral route'
            }],
            'text': '口服'
        },
        'dose': {
            'value': 500,
            'unit': 'mg',
            'system': 'http://unitsofmeasure.org',
            'code': 'mg',
        },
    }
    assert response_json_data[-1]['dosage'] == {
        'route': {
            'coding': [{
                'system': 'http://snomed.info/sct',
                'code': '26643006',
                'display': 'Oral route'
            }],
            'text': '口服'
        },
        'dose': {
            'value': 75,
            'unit': 'μg',
            'system': 'http://unitsofmeasure.org',
            'code': 'μg',
        },
    }

    assert response_json_data[0]['note'] == [{
        'time': '2025-03-01T00:00+08:00',
        'text': '飯後服用，治療呼吸道感染',
    }]
    assert response_json_data[-1]['note'] == [{
        'time': '2022-12-01T00:00+08:00',
        'text': '甲狀腺低下，空腹服用',
    }]

    assert response_json_data[0]['medicationCodeableConcept'] == {
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '323567000',
            'display': 'Amoxicillin (as amoxicillin sodium) 500 mg and clavulanic acid (as clavulanate potassium) 100 mg powder for solution for injection vial'
        }],
        'text': 'Amoxicillin (as amoxicillin sodium) 500 mg and clavulanic acid (as clavulanate potassium) 100 mg powder for solution for injection vial'
    }
    assert response_json_data[-1]['medicationCodeableConcept'] == {
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '768532006',
            'display': 'Levothyroxine-containing product'
        }],
        'text': 'Levothyroxine-containing product'
    }

    medication_admin_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
    response_json_data[0]['id'] = medication_admin_id
    payload = {
        'resource': response_json_data[0],
    }
    response = client.put(f'/api/v1/update/MedicationAdministration', headers=headers, json=payload)

    assert response.status_code == 201

    response = client.get(f'/api/v1/retrieve/MedicationAdministration?_id={medication_admin_id}', headers=headers)

    assert response.status_code == 200

@pytest.mark.dependency(depends=['test_upload_required_references'])
def test_analyze_upload_retrieve_questionnaire_response_cdr_data():
    module_name = 'CdrStatistics'
    json_data = []
    cdr_files = [
        'QuestionnaireResponse-ltc-questionnaire-response-cdr-complete-example.json',
        'QuestionnaireResponse-ltc-questionnaire-response-cdr-example.json',
        'QuestionnaireResponse-ltc-questionnaire-response-cdr-moderate-example.json',
    ]
    for cdr_file in cdr_files:
        with open(f'/app/app/tests/scenarios/{cdr_file}') as f:
            contents = f.read()
            json_data += json.loads(contents),
    payload = {
        'module_name': module_name,
        'data': json_data,
        'params': {},
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': 'API Key',
        'x-user': 'User',
    }

    response = client.post(f'/api/v1/analyze', headers=headers, json=payload)
    response_json = response.json()

    assert response.status_code == 200
    assert len(response_json['data'][0]) == 3
    assert response_json['data'][0][0]['result'] == 'Mild'
    assert response_json['data'][0][1]['result'] == 'Mild'
    assert response_json['data'][0][2]['result'] == 'Moderate'

    questionnaire_response_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
    json_data[0]['id'] = questionnaire_response_id
    payload = {
        'resource': json_data[0],
    }

    response = client.put('/api/v1/update/QuestionnaireResponse', headers=headers, json=payload)
    assert response.status_code == 201

    response = client.get(f'/api/v1/retrieve/QuestionnaireResponse?_id={questionnaire_response_id}', headers=headers)
    assert response.status_code == 200

@pytest.mark.dependency(depends=['test_upload_required_references'])
def test_convert_upload_retrieve_location_data():
    with open('/app/app/tests/scenarios/location.json') as f:
        ltc_location_data = f.read()

    module_name = 'LocationLtcConverter'
    payload = {
        'module_name': module_name,
        'original_data': json.loads(ltc_location_data),
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': 'API Key',
        'x-user': 'User',
    }

    response = client.post(f'/api/v1/convert', headers=headers, json=payload)
    response_json = response.json()
    response_json_data = response_json['data'][0]

    assert response.status_code == 200
    assert response_json['message'] == f'Converting data with {module_name} is successful.'
    assert len(response_json_data) == 10
    assert response_json_data[0]['name'] == '王大明'
    assert response_json_data[-1]['name'] == '周秀蘭'

    assert response_json_data[0]['description'] == '日照中心'
    assert response_json_data[-1]['description'] == '家裡'

    assert response_json_data[0]['address']['text'] == '新北市中和區安康路二段123號'
    assert response_json_data[-1]['address']['text'] == '新北市中和區安康路二段132號'

    assert response_json_data[0]['position']['longitude'] == 121.5170
    assert response_json_data[-1]['position']['longitude'] == 121.4874

    assert response_json_data[0]['position']['latitude'] == 25.0478
    assert response_json_data[-1]['position']['latitude'] == 25.0712

    location_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
    response_json_data[0]['id'] = location_id
    payload = {
        'resource': response_json_data[0],
    }

    response = client.put('/api/v1/update/Location', headers=headers, json=payload)
    assert response.status_code == 201

    response = client.get(f'/api/v1/retrieve/Location?_id={location_id}', headers=headers)
    assert response.status_code == 200

@pytest.mark.dependency(depends=['test_upload_required_references'])
def test_convert_upload_retrieve_adverse_event_data():
    with open('/app/app/tests/scenarios/adverse_event.json') as f:
        adverse_event_data = f.read()

    module_name = 'AdverseEventLtcConverter'
    payload = {
        'module_name': module_name,
        'original_data': json.loads(adverse_event_data),
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': 'API Key',
        'x-user': 'User',
    }

    response = client.post(f'/api/v1/convert', headers=headers, json=payload)
    response_json = response.json()
    response_json_data = response_json['data'][0]

    assert response.status_code == 200

    assert response_json_data[0]['extension'][0]['extension'][1]['valueString'] == '患者深夜獨自離開病房，試圖搭乘電梯返家'
    assert response_json_data[-1]['extension'][0]['extension'][1]['valueString'] == '患者對著鏡子持續與「陌生人」對話，出現明顯鏡像幻覺'

    assert response_json_data[0]['event']['text'] == '保全人員即時攔截，患者平安返回病房，已通知值班醫師及家屬，加裝手環定位追蹤'
    assert response_json_data[-1]['event']['text'] == '護理師移除鏡子或以布遮蓋，症狀緩解，回報醫師後記錄為鏡像幻覺，納入照護計畫調整'

    assert response_json_data[0]['date'] == '2024-04-01T01:22:00+08:00'
    assert response_json_data[-1]['date'] == '2024-04-10T22:50:00+08:00'

    assert response_json_data[0]['detected'] == '2024-04-01T01:22:00+08:00'
    assert response_json_data[-1]['detected'] == '2024-04-10T22:50:00+08:00'

    assert response_json_data[0]['recordedDate'] == '2024-04-01T01:22:00+08:00'
    assert response_json_data[-1]['recordedDate'] == '2024-04-10T22:50:00+08:00'

    adverse_event_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
    response_json_data[0]['id'] = adverse_event_id
    payload = {
        'resource': response_json_data[0],
    }

    response = client.put('/api/v1/update/AdverseEvent', headers=headers, json=payload)
    assert response.status_code == 201

    response = client.get(f'/api/v1/retrieve/AdverseEvent?_id={adverse_event_id}', headers=headers)
    assert response.status_code == 200
