import os
import json
import time
import pytest
import datetime
import subprocess


@pytest.mark.dependency()
def test_normal_circuit_states_for_create_upload_ltc_tw_2025_location_resource():
    normal_state_process = subprocess.Popen([
        'python3', '/app/app/tests/ltc_tw_2025/run_create_location_data_background_task.py',
    ])

    circuit_state_process = subprocess.Popen([
        'python3', '/app/app/tests/ltc_tw_2025/run_upload_location_circuit_background_task.py',
    ])

    broken_process = subprocess.Popen([
        'python3', '/app/app/tests/ltc_tw_2025/run_upload_location_broken_background_task.py',
    ])

    time.sleep(180)

    circuit_state_process.terminate()
    normal_state_process.terminate()
    broken_process.terminate()
