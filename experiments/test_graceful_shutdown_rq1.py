import time
import pytest
import subprocess
from python_on_whales import DockerClient


@pytest.mark.dependency()
def test_send_signal_via_python_on_whales_can_be_graceful_shutdown():
    subprocess.Popen([
        'python3', 'run_upload_location_data_background_task.py',
    ])

    docker = DockerClient(compose_files=['../docker-compose.yml'])

    docker.compose.start(services=['fhir_generator'])
    time.sleep(60)
    docker.compose.stop(services=['fhir_generator'], timeout=-1)
