import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_track13_2024_patient_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/track13_2024_patient.json', 'r', encoding='utf-8') as f:
        json_str = f.read()

    with open('/app/app/tests/expected_track13_2024_patient.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = {}
    json_dict['patient_payload'] = json.loads(json_str)
    response = client.post('/api/v1/track13_2024_patient', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']
    response_json['data'][0]['identifier'] = response_json['data'][0]['identifier'][0:-1]

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track13_2024_practitioner_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/track13_2024_practitioner.json', 'r', encoding='utf-8') as f:
        json_str = f.read()

    with open('/app/app/tests/expected_track13_2024_practitioner.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = {}
    json_dict['practitioner_payload'] = json.loads(json_str)
    response = client.post('/api/v1/track13_2024_practitioner', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track13_2024_goal_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/track13_2024_goal.json', 'r', encoding='utf-8') as f:
        json_str = f.read()

    with open('/app/app/tests/expected_track13_2024_goal.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = {}
    json_dict['goal_payload'] = json.loads(json_str)
    response = client.post('/api/v1/track13_2024_goal', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track13_2024_care_plan_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/track13_2024_care_plan.json', 'r', encoding='utf-8') as f:
        json_str = f.read()

    with open('/app/app/tests/expected_track13_2024_care_plan.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = {}
    json_dict['care_plan_payload'] = json.loads(json_str)
    response = client.post('/api/v1/track13_2024_care_plan', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track13_2024_condition_m_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/track13_2024_condition_m.json', 'r', encoding='utf-8') as f:
        json_str = f.read()

    with open('/app/app/tests/expected_track13_2024_condition_m.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = {}
    json_dict['condition_payload'] = json.loads(json_str)
    json_dict['condition_type'] = 'medical'
    response = client.post('/api/v1/track13_2024_condition', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track13_2024_condition_e_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/track13_2024_condition_e.json', 'r', encoding='utf-8') as f:
        json_str = f.read()

    with open('/app/app/tests/expected_track13_2024_condition_e.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = {}
    json_dict['condition_payload'] = json.loads(json_str)
    json_dict['condition_type'] = 'exercise'
    response = client.post('/api/v1/track13_2024_condition', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track13_2024_service_request_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/track13_2024_service_request.json', 'r', encoding='utf-8') as f:
        json_str = f.read()

    with open('/app/app/tests/expected_track13_2024_service_request.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = {}
    json_dict['service_request_payload'] = json.loads(json_str)
    response = client.post('/api/v1/track13_2024_service_request', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track13_2024_observation_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    with open('/app/app/tests/track13_2024_observation.json', 'r', encoding='utf-8') as f:
        json_str = f.read()

    with open('/app/app/tests/expected_track13_2024_observation.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = {}
    json_dict['observation_payload'] = json.loads(json_str)
    response = client.post('/api/v1/track13_2024_observation', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)
