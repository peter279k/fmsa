import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_calculate_average():
    module_name = 'AverageStatistics'
    payload = {
        'module_name': module_name,
        'data': [1, 2, 3],
        'params': {},
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/analyze', headers=headers, json=payload)
    response_json = response.json()

    expected = 2.0

    assert response.status_code == 200
    assert response_json['message'] == f'Analyzing data with {module_name} is successful.'
    assert response_json['data'][0] == expected
