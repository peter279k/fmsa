import time
import httpx
import pytest
import subprocess
import clickhouse_connect
from python_on_whales import DockerClient


@pytest.mark.dependency()
def test_send_signal_via_python_on_whales_can_be_graceful_shutdown():
    docker = DockerClient(compose_files=['../docker-compose.yml'])

    docker.compose.up(services=['fhir_data_manager'], detach=True)
    time.sleep(10)

    process = subprocess.Popen([
        'python3', 'run_upload_location_data_background_task.py',
    ])

    time.sleep(73)
    docker.compose.down(services=['fhir_data_manager'], timeout=-1)

    time.sleep(63)
    process.terminate()

@pytest.mark.dependency(depends=['test_send_signal_via_python_on_whales_can_be_graceful_shutdown'])
def test_that_the_id_should_be_in_the_fhir_database():
    docker = DockerClient(compose_files=['../docker-compose.yml'])

    docker.compose.up(services=['fhir_data_manager'], detach=True)
    time.sleep(10)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': 'API Key',
        'x-user': 'User',
    }
    client = clickhouse_connect.get_client(host='localhost', username='fmsa_exp', password='fmsa_exp')
    table_name = 'rq4_log_table'
    ch_sql = f'''
    SELECT resource_id FROM {table_name} where message = '201' order by timestamp
    '''
    location_data = client.query(ch_sql)

    for record in location_data.result_rows:
        resource_id = record[0]
        response = httpx.get(f'http://localhost:8081/api/v1/retrieve/Location?_id={resource_id}', headers=headers)
        assert response.status_code == 200
