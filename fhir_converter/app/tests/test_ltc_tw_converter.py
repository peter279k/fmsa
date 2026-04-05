import json
import pytest
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

@pytest.mark.dependency()
def test_convert_location_data():
    with open('/app/app/tests/ltc_tw_2025/location.json') as f:
        ltc_location_data = f.read()

    module_name = 'LocationLtcConverter'
    payload = {
        'module_name': module_name,
        'original_data': json.loads(ltc_location_data),
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
    assert response_json_data[-1]['address']['text'] == '新北市中和區安康路二段132號'

    assert response_json_data[0]['position']['longitude'] == 121.5170
    assert response_json_data[-1]['position']['longitude'] == 121.4874

    assert response_json_data[0]['position']['latitude'] == 25.0478
    assert response_json_data[-1]['position']['latitude'] == 25.0712

@pytest.mark.dependency
def test_convert_adverse_event_data():
    with open('/app/app/tests/ltc_tw_2025/adverse_event.json') as f:
        adverse_event_data = f.read()

    module_name = 'AdverseEventLtcConverter'
    payload = {
        'module_name': module_name,
        'original_data': json.loads(adverse_event_data),
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/convert', headers=headers, json=payload)
    response_json = response.json()
    response_json_data = response_json['data'][0]

    assert response.status_code == 200

    assert response_json_data[0]['extension'][0]['extension'][1]['valueString'] == '患者深夜獨自離開病房，試圖搭乘電梯返家'
    assert response_json_data[-1]['extension'][0]['extension'][1]['valueString'] == '患者對著鏡子持續與「陌生人」對話，出現明顯鏡像幻覺'

    assert response_json_data[0]['event'] == '保全人員即時攔截，患者平安返回病房，已通知值班醫師及家屬，加裝手環定位追蹤'
    assert response_json_data[-1]['event'] == '護理師移除鏡子或以布遮蓋，症狀緩解，回報醫師後記錄為鏡像幻覺，納入照護計畫調整'

    assert response_json_data[0]['date'] == '2024-04-01T01:22:00+08:00'
    assert response_json_data[-1]['date'] == '2024-04-10T22:50:00+08:00'

    assert response_json_data[0]['detected'] == '2024-04-01T01:22:00+08:00'
    assert response_json_data[-1]['detected'] == '2024-04-10T22:50:00+08:00'

    assert response_json_data[0]['recordedDate'] == '2024-04-01T01:22:00+08:00'
    assert response_json_data[-1]['recordedDate'] == '2024-04-10T22:50:00+08:00'
