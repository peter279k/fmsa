import time
import json
import httpx
import datetime
import clickhouse_connect


client = clickhouse_connect.get_client(host='localhost', username='fmsa_exp', password='fmsa_exp')
table_name = 'rq1_log_table'
columns = ['timestamp', 'message_type', 'message']
log_table = f'''
CREATE TABLE IF NOT EXISTS {table_name}
(
    timestamp DateTime DEFAULT now(),
    message_type String,
    message String
)
ENGINE = Log
'''
clean_log_table = f'TRUNCATE TABLE {table_name}'

client.query(log_table)
client.query(clean_log_table)


while True:
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': 'API Key',
        'x-user': 'User',
    }
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

    with open('./Location-ltc-location-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['text']
    del expected_json['id']

    json_dict = {}
    json_dict['payload'] = payload
    response = httpx.post('http://localhost:8081/api/v1/ltc_tw_2025_location', headers=headers, json=json_dict)

    try:
        assert response.status_code == 200
        records = [
            [datetime.datetime.now(datetime.UTC), 'success', str(response.status_code)],
        ]
    except Exception:
        records = [
            [datetime.datetime.now(datetime.UTC), 'error', str(response.status_code)],
        ]

    client.insert(table_name, records, column_names=columns)
    record = records[0]
    record[0] = str(int(record[0].timestamp()))
    print(f'Data: {",".join(record)} is inserted.')

    time.sleep(1)
