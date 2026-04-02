import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_ltc_tw_2025_medication_administration_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {
        'resourceType': 'MedicationAdministration',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCMedicationAdministration'],
        'status': 'completed',
        'medication_codeable_concept_coding': [{
            'system': 'http://snomed.info/sct',
            'code': '323402006',
            'display': 'Product containing benethamine penicillin (medicinal product)'
        }],
        'medication_codeable_concept_text': 'Product containing benethamine penicillin (medicinal product)',
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'effective_date_time': '2024-01-15T08:00:00+08:00',
        'performer': [{
            'actor': {
                'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
            }
        }],
        'note': [{
            'time': '2024-01-15T08:00:00+08:00',
            'text': '住民按時服藥，無不良反應'
        }],
        'dosage': {
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
                'code': 'mg'
            }
        }
    }

    with open('/app/app/tests/ltc_tw_2025/MedicationAdministration-ltc-medication-administration-metformin-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    response = client.post('/api/v1/ltc_tw_2025_medication_administration', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['note']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json
