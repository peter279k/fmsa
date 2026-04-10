import time
import pytest
import subprocess
from python_on_whales import DockerClient


@pytest.fixture(scope='function')
def run_background_task():
    process = subprocess.Popen([
        'python3', 'run_upload_location_data_background_task.py',
    ])

    yield process

@pytest.mark.dependency()
def test_send_signal_via_python_on_whales_can_be_graceful_shutdown():
    time.sleep(5)
    docker = DockerClient(compose_files=['../docker-compose.yml'])
    docker.compose.stop(services=['fhir_generator'], timeout=-1)
