import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_ltc_tw_2025_adverse_event_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    extension = [{
        'extension': [{
            'url': 'textType',
            'valueCodeableConcept': {
                'coding': [{
                    'system': 'http://ltc-ig.fhir.tw/CodeSystem/cs-tw-ltc-incident-texttype',
                    'code': 'desc',
                    'display': '事件描述'
                }]
            }
        },
        {
            'url': 'text',
            'valueString': '巡視時發現個案暈眩跌坐於地，已聯繫家屬與機構。'
        }],
        'url': 'http://ltc-ig.fhir.tw/StructureDefinition/Ext-TW-LTC-AdverseEvent-Description'
    }]
    identifiers = [
        {
            'use': 'official',
            'system': 'http://ltc-ig.fhir.tw/adverse-event',
            'value': 'AE-CS100-2025-001'
        },
        {
            'use': 'official',
            'system': 'http://ltc-ig.fhir.tw/adverse-event',
            'value': 'AE-2024-001'
        },
    ]
    events = [
        {
            'coding': [{
                'system': 'http://ltc-ig.fhir.tw/CodeSystem/cs-tw-ltc-incident-category',
                'code': 'careacc',
                'display': '照顧意外事件'
            }]
        },
        {
            'text': '離開安全區域',
        },
    ]
    subjects = [
        {
            'reference': 'Patient/ltc-patient-cs100-example'
        },
        {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
    ]
    dates = ['2025-11-05T10:20:00+08:00', '2024-01-15T14:30:00+08:00']
    detected = '2024-01-15T14:32:00+08:00'
    recorded_dates = ['2025-11-05T10:30:00+08:00', '2024-01-15T14:35:00+08:00']
    actuality = 'actual'
    location = {
        'reference': 'Location/ltc-location-example'
    }
    seriousness = {
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/adverse-event-seriousness',
            'code': 'serious',
            'display': 'Serious'
        }]
    }
    severity = {
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/adverse-event-severity',
            'code': 'moderate',
            'display': 'Moderate'
        }]
    }
    outcome = {
        'coding': [{
            'system': 'http://terminology.hl7.org/CodeSystem/adverse-event-outcome',
            'code': 'recovering',
            'display': 'Recovering'
        }]
    }
    recorder = {
        'reference': 'Practitioner/ltc-practitioner-example'
    }

    payload_template = {
        'resourceType': 'AdverseEvent',
        'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/AdverseEvent-twltc'],
        'extension': [],
        'identifier': {},
        'actuality': 'actual',
        'event': {},
        'subject': {},
        'date': '',
        'detected': '',
        'recorded_date': '',
        'location': {},
        'seriousness': {},
        'severity': {},
        'outcome': {},
        'recorder': {},
    }

    expected_payload = {
        'resourceType': 'AdverseEvent',
        'meta': {
            'profile': ['http://ltc-ig.fhir.tw/StructureDefinition/AdverseEvent-twltc']
        },
        'extension': [],
        'identifier': {},
        'actuality': 'actual',
        'event': {},
        'subject': {},
        'date': '',
        'detected': '',
        'recordedDate': '',
        'location': {},
        'seriousness': {},
        'severity': {},
        'outcome': {},
        'recorder': {},
    }

    expected = dict(expected_payload)
    expected['extension'] = extension
    expected['identifier'] = identifiers[0]
    expected['event'] = events[0]
    expected['subject'] = subjects[0]
    expected['date'] = dates[0]
    expected['recordedDate'] = recorded_dates[0]

    del expected['detected']
    del expected['location']
    del expected['seriousness']
    del expected['severity']
    del expected['outcome']
    del expected['recorder']

    payload = dict(payload_template)
    payload['extension'] = extension
    payload['identifier'] = identifiers[0]
    payload['event'] = events[0]
    payload['subject'] = subjects[0]
    payload['date'] = dates[0]
    payload['recorded_date'] = recorded_dates[0]

    json_dict = {}
    json_dict['payload'] = payload
    json_dict['type'] = 'cs100'
    response = client.post('/api/v1/ltc_tw_2025_adverse_event', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['extension']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected

    expected = dict(expected_payload)
    expected['identifier'] = identifiers[1]
    expected['event'] = events[1]
    expected['subject'] = subjects[1]
    expected['date'] = dates[1]
    expected['detected'] = detected
    expected['recordedDate'] = recorded_dates[1]
    expected['location'] = location
    expected['seriousness'] = seriousness
    expected['severity'] = severity
    expected['outcome'] = outcome
    expected['recorder'] = recorder
    del expected['extension']

    payload = dict(payload_template)
    payload['extension'] = extension
    payload['identifier'] = identifiers[1]
    payload['actuality'] = actuality
    payload['event'] = events[1]
    payload['subject'] = subjects[1]
    payload['date'] = dates[1]
    payload['detected'] = detected
    payload['location'] = location
    payload['seriousness'] = seriousness
    payload['severity'] = severity
    payload['outcome'] = outcome
    payload['recorder'] = recorder
    payload['recorded_date'] = recorded_dates[1]

    json_dict = {}
    json_dict['payload'] = payload
    json_dict['type'] = 'ltc'
    response = client.post('/api/v1/ltc_tw_2025_adverse_event', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['extension']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected
