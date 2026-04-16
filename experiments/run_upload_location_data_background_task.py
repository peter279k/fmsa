import time
import json
import httpx
import hashlib
import secrets
import datetime
import clickhouse_connect


client = clickhouse_connect.get_client(host='localhost', username='fmsa_exp', password='fmsa_exp')
table_name = 'rq4_log_table'
columns = ['timestamp', 'message_type', 'message', 'resource_id']
log_table = f'''
CREATE TABLE IF NOT EXISTS {table_name}
(
    timestamp DateTime DEFAULT now(),
    message_type String,
    message String,
    resource_id String
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

    with open('./Location-ltc-location-example.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    expected_json = json.loads(expected_json_str)
    del expected_json['id']

    json_dict = {}
    location_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
    expected_json['id'] = location_id
    json_dict['resource'] = expected_json
    response = httpx.put('http://localhost:8081/api/v1/update/Location', headers=headers, json=json_dict)

    try:
        assert response.status_code == 201
        records = [
            [datetime.datetime.now(datetime.UTC), 'success', str(response.status_code), location_id],
        ]
    except Exception:
        records = [
            [datetime.datetime.now(datetime.UTC), 'error', str(response.status_code), location_id],
        ]

    client.insert(table_name, records, column_names=columns)
    record = records[0]
    record[0] = str(int(record[0].timestamp()))
    print(f'Data: {",".join(record)} is inserted.')

    time.sleep(1)
