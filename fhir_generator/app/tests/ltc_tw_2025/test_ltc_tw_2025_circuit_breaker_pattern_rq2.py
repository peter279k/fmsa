import os
import json
import time
import pytest
import datetime
from app.main import app
import clickhouse_connect
from fastapi.testclient import TestClient


client = TestClient(app)

host = os.getenv('IP_ADDRESS', 'localhost')
db_client = clickhouse_connect.get_client(host=host, username='fmsa_exp', password='fmsa_exp')
table_name = 'rq2_log_table'
columns = ['timestamp', 'message_type', 'message']
log_table = f'''
CREATE TABLE IF NOT EXISTS {table_name}
(
    timestamp DateTime64(3, 'UTC') DEFAULT now(),
    message_type String,
    message String
)
ENGINE = Log
'''
clean_log_table = f'TRUNCATE TABLE {table_name}'

db_client.query(log_table)
db_client.query(clean_log_table)

@pytest.mark.dependency()
def test_closed_state_create_ltc_tw_2025_location_resource():
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

    assert len(response_json['data'][0]['type']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected_json

    records = [
        [datetime.datetime.now(datetime.UTC), 'closed state', str(response.status_code)],
    ]
    db_client.insert(table_name, records, column_names=columns)

    record = records[0]
    record[0] = str(int(record[0].timestamp()));

    print(f'Closed state: {",".join(record)}')

@pytest.mark.dependency(depends=['test_closed_state_create_ltc_tw_2025_location_resource'])
def test_open_state_create_ltc_tw_2025_location_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = {'resource': 'invalid FHIR Resource'}

    with open('/app/app/tests/ltc_tw_2025/Location-ltc-location-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    exception_msg = '503: The system is experiencing high failure rates. Please try again later.'

    # open state
    for _ in range(5):
        try: 
            response = client.post('/api/v1/ltc_tw_2025_location', headers=headers, json=json_dict)
        except Exception as e:
            assert exception_msg == str(e)

            records = [
                    [datetime.datetime.now(datetime.UTC), 'open state', exception_msg],
            ]

            db_client.insert(table_name, records, column_names=columns)
            record = records[0]
            record[0] = str(int(record[0].timestamp()));
            print(f'Open state: {",".join(record)}')

    json_dict = {}
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

    json_dict['payload'] = payload
    seconds = 60
    timeout_exception_msg = '503: Retry after 59 secs'

    # half open state for retry timeout
    try:
        client.post('/api/v1/ltc_tw_2025_location', headers=headers, json=json_dict)
    except Exception as e:
        assert timeout_exception_msg == str(e)

        records = [
            [datetime.datetime.now(datetime.UTC), 'half open state', timeout_exception_msg],
        ]

        db_client.insert(table_name, records, column_names=columns)
        record = records[0]
        record[0] = str(int(record[0].timestamp()));
        print(f'Half open state: {",".join(record)}')

    time.sleep(seconds)

    # change into closed state
    response = client.post('/api/v1/ltc_tw_2025_location', headers=headers, json=json_dict)

    assert response.status_code == 200

    records = [
        [datetime.datetime.now(datetime.UTC), 'closed state', str(response.status_code)],
    ]

    db_client.insert(table_name, records, column_names=columns)
    record = records[0]
    record[0] = str(int(record[0].timestamp()));
    print(f'Closed state: {",".join(record)}')

    db_client.close()
