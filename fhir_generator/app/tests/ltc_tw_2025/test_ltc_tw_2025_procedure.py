import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_ltc_tw_2025_procedure_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload_template = {
        'resourceType': 'Procedure',
        'id': 'ltc-procedure-bathing-example',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCProcedureCareActivity'],
        'status': 'completed',
        'code_codings': [],
        'code_texts': '',
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'performed_date_time': '2024-01-15T14:30:00+08:00',
        'performer': [{
            'actor': {
                'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
            }
        }],
        'note': [{
            'time': '2024-01-15T14:30:00+08:00',
            'text': '住民配合度良好，無特殊狀況'
        }]
    }
    code_codings = [
        [{
            'system': 'http://snomed.info/sct',
            'code': '226010006',
            'display': 'Assisting with eating and drinking'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '60369001',
            'display': 'Bathing patient'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '225964003',
            'display': 'Assisting with personal hygiene'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '313332003',
            'display': 'Dressing patient'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '313420001',
            'display': 'Assisting with toileting'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '223454002',
            'display': 'Escorting subject to toilet'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '710803000',
            'display': 'Assistance with mobility'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '713138001',
            'display': 'Assistance with mobility in bed'
        }],
        [{
            'system': 'http://snomed.info/sct',
            'code': '733923007',
            'display': 'Change of diaper'
        }],
    ]
    code_texts = [
        '進食協助',
        '沐浴/擦澡',
        '個人衛生協助',
        '穿衣',
        '如廁協助',
        '陪同到廁所',
        '移位/移動協助',
        '床上移動協助',
        '更換尿布',
    ]
    with open('/app/app/tests/ltc_tw_2025/Procedure-ltc-procedure-bathing-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    for index,_ in enumerate(code_texts):
        payload_template['code_codings'] = code_codings[index]
        payload_template['code_texts'] = code_texts[index]

        expected_json = json.loads(expected_json_str)
        expected_json['code_codings'] = code_codings[index]
        expected_json['code_texts'] = code_texts[index]
        del expected_json['text']
        del expected_json['id']

        json_dict = {}
        json_dict['payload'] = payload_template
        response = client.post('/api/v1/ltc_tw_2025_practitioner_role', headers=headers, json=json_dict)

        response_json = response.json()
        del response_json['data'][0]['id']

        assert len(response_json['data'][0]['availableTime']) == 1
        assert len(response_json['data'][0]['telecom']) == 2

        assert response.status_code == 200
        assert len(response_json['data']) == 1
        assert response_json['data'][0] == expected_json
