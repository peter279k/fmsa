import time
import pytest
import subprocess
from python_on_whales import DockerClient


@pytest.mark.dependency()
def test_send_signal_via_python_on_whales_can_be_graceful_shutdown():
    docker = DockerClient(compose_files=['../docker-compose.yml'])

    docker.compose.up(services=['fhir_generator'], detach=True)
    time.sleep(5)

    process = subprocess.Popen([
        'python3', 'run_upload_location_data_background_task.py',
    ])

    time.sleep(62)
    docker.compose.down(services=['fhir_generator'], timeout=-1)

    time.sleep(1)
    process.terminate()
