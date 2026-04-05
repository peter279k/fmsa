import json
import pytest
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

@pytest.mark.dependency()
def test_convert_location_data():
    with open('/app/app/tests/ltc_tw_2025/location.json') as f:
        golden_smart_home_data = f.read()

    module_name = 'LocationLtcConverter'
    payload = {
        'module_name': module_name,
        'original_data': json.loads(golden_smart_home_data),
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/convert', headers=headers, json=payload)
    response_json = response.json()
    response_json_data = response_json['data'][0]

    assert response.status_code == 200
    assert response_json['message'] == f'Converting data with {module_name} is successful.'
    assert len(response_json_data) == 10
    assert response_json_data[0]['name'] == '王大明'
    assert response_json_data[-1]['name'] == '周秀蘭'

    assert response_json_data[0]['description'] == '日照中心'
    assert response_json_data[-1]['description'] == '家裡'

    assert response_json_data[0]['address']['text'] == '新北市中和區安康路二段123號'
    assert response_json_data[-1]['address']['text'] == '新北市中和區安康路二段133號'

    assert response_json_data[0]['longitude'] == 121.5170
    assert response_json_data[-1]['longitude'] == 121.4874

    assert response_json_data[0]['latitude'] == 25.0478
    assert response_json_data[-1]['latitude'] == 25.0712
