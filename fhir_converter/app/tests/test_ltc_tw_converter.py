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

    assert response_json_data[0]['event']['text'] == '保全人員即時攔截，患者平安返回病房，已通知值班醫師及家屬，加裝手環定位追蹤'
    assert response_json_data[-1]['event']['text'] == '護理師移除鏡子或以布遮蓋，症狀緩解，回報醫師後記錄為鏡像幻覺，納入照護計畫調整'

    assert response_json_data[0]['date'] == '2024-04-01T01:22:00+08:00'
    assert response_json_data[-1]['date'] == '2024-04-10T22:50:00+08:00'

    assert response_json_data[0]['detected'] == '2024-04-01T01:22:00+08:00'
    assert response_json_data[-1]['detected'] == '2024-04-10T22:50:00+08:00'

    assert response_json_data[0]['recordedDate'] == '2024-04-01T01:22:00+08:00'
    assert response_json_data[-1]['recordedDate'] == '2024-04-10T22:50:00+08:00'

@pytest.mark.dependency
def test_convert_procedure_data():
    with open('/app/app/tests/ltc_tw_2025/procedure.json') as f:
        procedure_data = f.read()

    module_name = 'ProcedureLtcConverter'
    payload = {
        'module_name': module_name,
        'original_data': json.loads(procedure_data),
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/convert', headers=headers, json=payload)
    response_json = response.json()
    response_json_data = response_json['data'][0]

    assert response.status_code == 200

    assert response_json_data[0]['performedDateTime'] == '2025-03-01T08:00+08:00'
    assert response_json_data[-1]['performedDateTime'] == '2025-03-05T19:00+08:00'

    assert response_json_data[0]['code'] == {
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '225964003',
            'display': 'Assisting with personal hygiene'
        }],
        'text': '個人衛生協助',
    }
    assert response_json_data[-1]['code'] == {
        'coding': [{
            'system': 'http://snomed.info/sct',
            'code': '225964003',
            'display': 'Assisting with personal hygiene'
        }],
        'text': '個人衛生協助',
    }

    assert response_json_data[0]['note'] == [{
        'time': '2025-03-01T08:00+08:00',
        'text': '合作度佳，情緒穩定',
    }]
    assert response_json_data[-1]['note'] == [{
        'time': '2025-03-05T19:00+08:00',
        'text': '情緒平靜，表示願意休息',
    }]

@pytest.mark.dependency
def test_convert_medication_administration_data():
    with open('/app/app/tests/ltc_tw_2025/medication_administration.json') as f:
        medication_admin_data = f.read()

    medication_lists = json.loads(medication_admin_data)['用藥紀錄']
    module_name = 'MedicationAdministrationLtcConverter'
    payload = {
        'module_name': module_name,
        'original_data': medication_lists,
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.post(f'/api/v1/convert', headers=headers, json=payload)
    response_json = response.json()
    response_json_data = response_json['data'][0]

    assert response.status_code == 200

    assert response_json_data[0]['effectiveDateTime'] == '2025-03-01T00:00+08:00'
    assert response_json_data[-1]['effectiveDateTime'] == '2022-12-01T00:00+08:00'
