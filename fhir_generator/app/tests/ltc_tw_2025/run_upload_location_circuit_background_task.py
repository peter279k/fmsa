import os
import time
import json
import httpx
import secrets
import datetime
import clickhouse_connect


host = os.getenv('IP_ADDRESS', '172.17.0.1')
client = clickhouse_connect.get_client(host=host, username='fmsa_exp', password='fmsa_exp')
table_name = 'rq5_log_table_circuit'
columns = ['timestamp', 'message_type', 'message', 'service_name', 'api_path']
log_table = f'''
CREATE TABLE IF NOT EXISTS {table_name}
(
    timestamp DateTime DEFAULT now(),
    message_type String,
    message String,
    service_name String,
    api_path String
)
ENGINE = Log
'''
clean_log_table = f'TRUNCATE TABLE {table_name}'

client.query(log_table)
client.query(clean_log_table)


state = ''
error_counter = 0
while True:
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
    json_dict['resource_name'] = 'Location'
    if state == 'Closed':
        json_dict['resource_name'] = 'OpenState'
        error_counter += 1
        if error_counter == 5:
            error_counter = 0
            state = 'OpenState'
    elif state == 'OpenState':
        json_dict['resource_name'] = 'Location'

    response = httpx.post(
        'http://fhir_generator:8000/circuit/api/v1/ltc_tw_2025_location_circuit',
        headers=headers,
        json=json_dict
    )

    if response.status_code == 200:
        response_json = response.json()
        records = [
            [
                datetime.datetime.now(datetime.UTC), 'closed state',
                str(response.status_code), 'fhir_generator', 'ltc_tw_2025_location_circuit',
            ],
        ]
        client.insert(table_name, records, column_names=columns)

        record = records[0]
        record[0] = str(int(record[0].timestamp()));

        state = 'Closed'
    else:
        records = [
            [
                datetime.datetime.now(datetime.UTC), 'open/half-open state',
                str(response.status_code), 'fhir_generator', 'ltc_tw_2025_location_circuit',
            ],
        ]

    print(f'Closed state: {",".join(record)}')
    time.sleep(1)
