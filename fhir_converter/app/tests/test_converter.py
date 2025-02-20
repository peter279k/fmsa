import json
import pytest
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

@pytest.mark.dependency()
def test_import_archived_code_system():
    with open('/app/app/tests/sport.raw_data_goldensmarthome_20241212.json') as f:
        golden_smart_home_data = f.read()

    with open('/app/app/tests/expected_sport.raw_data_goldensmarthome_20241212.json') as f:
        expected_converted_json = f.read()

    module_name = 'GoldenSmartHomeConverter'
    payload = {
        'module_name': module_name,
        'original_data': json.loads(golden_smart_home_data),
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/convert', headers=headers, json=payload)
    response_json = response.json()

    expected_converted_json_list = json.loads(expected_converted_json)

    assert response.status_code == 200
    assert response_json['message'] == f'Converting data with {module_name} is successful.'
    assert len(response_json['data'][0]) == len(expected_converted_json_list)
    assert response_json['data'][0][1] == expected_converted_json_list[2]
