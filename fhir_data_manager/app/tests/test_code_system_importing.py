import subprocess
from app.main import app
from urllib.parse import urlencode
from fastapi.testclient import TestClient


processed_id = ''
client = TestClient(app)

def test_import_archived_code_system():
    filename = {
        'filename': 'Loinc_2.72.zip'
    }
    encoded_uri = urlencode(filename)

    upload_archived_code_system = 'curl -F "zip_file=@/app/app/tests/Loinc_2.72.zip" http://terminology_manager:8000/api/v1/upload_terminology'.split(' ')
    uploaded_result = subprocess.run(upload_archived_code_system, capture_output=True)

    assert uploaded_result.returncode == 0

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.get(f'/api/v1/import_archived_code_system?{encoded_uri}', headers=headers)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json['message'] == 'Importing the {} is on the way.'.format(filename['filename'])
    assert len(response['data']) == 1
    assert type(response['data'][0]['processed_id']) is str

    global processed_id
    processed_id = response['data'][0]['processed_id']
