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

def test_calculate_geometric_mean():
    module_name = 'GeometricMeanStatistics'
    payload = {
        'module_name': module_name,
        'data': [1, 2, 3],
        'params': {},
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/analyze', headers=headers, json=payload)
    response_json = response.json()

    expected_rounded_value = 1.8
    precision = 1

    assert response.status_code == 200
    assert response_json['message'] == f'Analyzing data with {module_name} is successful.'
    assert round(response_json['data'][0], precision) == expected_rounded_value

def test_calculate_harmonic_mean():
    module_name = 'HarmonicMeanStatistics'
    payload = {
        'module_name': module_name,
        'data': [1, 2, 3],
        'params': {},
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/analyze', headers=headers, json=payload)
    response_json = response.json()

    expected_rounded_value = 1.6
    precision = 1

    assert response.status_code == 200
    assert response_json['message'] == f'Analyzing data with {module_name} is successful.'
    assert round(response_json['data'][0], precision) == expected_rounded_value

def test_calculate_median():
    module_name = 'MedianStatistics'
    payload = {
        'module_name': module_name,
        'data': [1, 2, 3, 4],
        'params': {},
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/analyze', headers=headers, json=payload)
    response_json = response.json()

    expected = 2.5

    assert response.status_code == 200
    assert response_json['message'] == f'Analyzing data with {module_name} is successful.'
    assert response_json['data'][0] == expected

def test_calculate_mode():
    module_name = 'ModeStatistics'
    payload = {
        'module_name': module_name,
        'data': [1, 2, 3, 3, 3],
        'params': {},
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/analyze', headers=headers, json=payload)
    response_json = response.json()

    expected = 3

    assert response.status_code == 200
    assert response_json['message'] == f'Analyzing data with {module_name} is successful.'
    assert response_json['data'][0] == expected

def test_stdev_mode_without_xbar():
    module_name = 'StdevStatistics'
    payload = {
        'module_name': module_name,
        'data': [1, 2, 3, 3, 3],
        'params': {},
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/analyze', headers=headers, json=payload)
    response_json = response.json()

    expected_rounded_value = 0.9
    precision = 1

    assert response.status_code == 200
    assert response_json['message'] == f'Analyzing data with {module_name} is successful.'
    assert round(response_json['data'][0], precision) == expected_rounded_value

def test_stdev_mode_with_xbar():
    module_name = 'StdevStatistics'
    payload = {
        'module_name': module_name,
        'data': [1, 2, 3, 3, 3],
        'params': {'xbar': 1},
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/analyze', headers=headers, json=payload)
    response_json = response.json()

    expected_rounded_value = 1.8
    precision = 1

    assert response.status_code == 200
    assert response_json['message'] == f'Analyzing data with {module_name} is successful.'
    assert round(response_json['data'][0], precision) == expected_rounded_value
