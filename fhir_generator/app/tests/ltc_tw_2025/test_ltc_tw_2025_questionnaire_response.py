import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_ltc_tw_2025_questionnaire_response_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload_template = {
        'resourceType': 'QuestionnaireResponse',
        'profile_urls': [],
        'extension': [],
        'questionnaire': '',
        'status': 'completed',
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'authored': '',
        'author': {
            'reference': 'Practitioner/ltc-practitioner-physician-aa12-example'
        },
        'source': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'item': [],
    }
    expected_payload_template = {
        'resourceType': 'QuestionnaireResponse',
        'meta': {
            'profile': []
        },
        'extension': [],
        'questionnaire': '',
        'status': 'completed',
        'subject': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'authored': '',
        'author': {
            'reference': 'Practitioner/ltc-practitioner-physician-aa12-example'
        },
        'source': {
            'reference': 'Patient/ltc-patient-chen-ming-hui'
        },
        'item': [],
    }
    profile_urls = [
        ['http://ltc-ig.fhir.tw/StructureDefinition/LTCQuestionnaireResponseCDR'],

        ['http://ltc-ig.fhir.tw/StructureDefinition/LTCQuestionnaireResponseMMSE'],
    ]
    extensions = [
        [{
            'url': 'http://ltc-ig.fhir.tw/StructureDefinition/cdr-total-score',
            'valueInteger': 2
        }],
        [{
            'url': 'http://ltc-ig.fhir.tw/StructureDefinition/cdr-total-score',
            'valueInteger': 1
        }],
        [{
            'url': 'http://ltc-ig.fhir.tw/StructureDefinition/cdr-total-score',
            'valueInteger': 1
        }],

        [{
            'url': 'http://ltc-ig.fhir.tw/StructureDefinition/mmse-total-score',
            'valueInteger': 28
        }],
        [{
            'url': 'http://ltc-ig.fhir.tw/StructureDefinition/mmse-total-score',
            'valueInteger': 30
        }],
        [{
            'url': 'http://ltc-ig.fhir.tw/StructureDefinition/mmse-total-score',
            'valueInteger': 13
        }],
    ]
    questionnaires = [
        'http://ltc-ig.fhir.tw/Questionnaire/ltc-questionnaire-cdr',
        'http://ltc-ig.fhir.tw/Questionnaire/ltc-questionnaire-mmse',
    ]
    authored_lists = [
        '2024-01-15T10:30:00+08:00',
        '2024-01-15T10:30:00+08:00',
        '2024-01-15T10:30:00+08:00',

        '2024-01-15T10:30:00+08:00',
        '2024-01-15T14:30:00+08:00',
        '2024-01-15T14:30:00+08:00',
    ]
    mmse_items = [
    [{
        'linkId': 'MMSE-1',
        'text': '今年是那一年?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-2',
        'text': '現在是什麼季節?',
        'answer': [{
                'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-3',
        'text': '今天是幾號?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-4',
        'text': '今天是禮拜幾?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-5',
        'text': '現在是那一個月份?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-6',
        'text': '我們現在是在那一個省?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-7',
        'text': '我們現在是在那一個縣、市?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-8',
        'text': '這裡屬於哪一個區或是鄉鎮?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-9',
        'text': '這個社區單位(醫院、診所)的名稱?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-10',
        'text': '現在我們是在幾樓?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-11',
        'text': '請重複這三個名稱,按第一次複述結果計分',
        'answer': [{
            'valueInteger': 3
        }]
    },
    {
        'linkId': 'MMSE-12',
        'text': '請從100開始連續減7,一直減7直到我說停為止。(每減對一次得一分)',
        'answer': [{
            'valueInteger': 5
        }]
    },
    {
        'linkId': 'MMSE-13',
        'text': '藍色',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-14',
        'text': '悲傷',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-15',
        'text': '火車',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-16',
        'text': '(拿出手錶)這是什麼?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-17',
        'text': '(拿出鉛筆)這是什麼?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-18',
        'text': '請跟我唸一句話『白紙真正寫黑字』',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-19',
        'text': '請唸一遍並做做看『請閉上眼睛』',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-20',
        'text': '請用左/右手(非利手)拿這張紙(三步驟指令,每對一步驟得一分)',
        'answer': [{
            'valueInteger': 3
        }]
    },
    {
        'linkId': 'MMSE-21',
        'text': '請在紙上寫一句語意完整的句子。(含主詞動詞且語意完整的句子)',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-22',
        'text': '這裡有一個圖形,請在旁邊畫出一個相同的圖形。(兩五邊形,交一四邊形,有兩交點,則給分)',
        'answer': [{
            'valueInteger': 1
        }]
    }],
    [{
        'linkId': 'MMSE-1',
        'text': '今年是那一年?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-2',
        'text': '現在是什麼季節?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-3',
        'text': '今天是幾號?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-4',
        'text': '今天是禮拜幾?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-5',
        'text': '現在是那一個月份?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-6',
        'text': '我們現在是在那一個省?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-7',
        'text': '我們現在是在那一個縣、市?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-8',
        'text': '這裡屬於哪一個區或是鄉鎮?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-9',
        'text': '這個社區單位(醫院、診所)的名稱?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-10',
        'text': '現在我們是在幾樓?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-11',
        'text': '請重複這三個名稱,按第一次複述結果計分',
        'answer': [{
            'valueInteger': 3
        }]
    },
    {
        'linkId': 'MMSE-12',
        'text': '請從100開始連續減7,一直減7直到我說停為止。(每減對一次得一分)',
        'answer': [{
            'valueInteger': 5
        }]
    },
    {
        'linkId': 'MMSE-13',
        'text': '藍色',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-14',
        'text': '悲傷',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-15',
        'text': '火車',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-16',
        'text': '(拿出手錶)這是什麼?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-17',
        'text': '(拿出鉛筆)這是什麼?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-18',
        'text': '請跟我唸一句話『白紙真正寫黑字』',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-19',
        'text': '請唸一遍並做做看『請閉上眼睛』',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-20',
        'text': '請用左/右手(非利手)拿這張紙(三步驟指令,每對一步驟得一分)',
        'answer': [{
            'valueInteger': 3
        }]
    },
    {
        'linkId': 'MMSE-21',
        'text': '請在紙上寫一句語意完整的句子。(含主詞動詞且語意完整的句子)',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-22',
        'text': '這裡有一個圖形,請在旁邊畫出一個相同的圖形。(兩五邊形,交一四邊形,有兩交點,則給分)',
        'answer': [{
            'valueInteger': 1
        }]
    }],
    [{
        'linkId': 'MMSE-1',
        'text': '今年是那一年?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-2',
        'text': '現在是什麼季節?',
        'answer': [{
            'valueInteger': 0
        }]
    },
    {
        'linkId': 'MMSE-3',
        'text': '今天是幾號?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-4',
        'text': '今天是禮拜幾?',
        'answer': [{
            'valueInteger': 0
        }]
    },
    {
        'linkId': 'MMSE-5',
        'text': '現在是那一個月份?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-6',
        'text': '我們現在是在那一個省?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-7',
        'text': '我們現在是在那一個縣、市?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-8',
        'text': '這裡屬於哪一個區或是鄉鎮?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-9',
        'text': '這個社區單位(醫院、診所)的名稱?',
        'answer': [{
            'valueInteger': 0
        }]
    },
    {
        'linkId': 'MMSE-10',
        'text': '現在我們是在幾樓?',
        'answer': [{
            'valueInteger': 0
        }]
    },
    {
        'linkId': 'MMSE-11',
        'text': '請重複這三個名稱,按第一次複述結果計分',
        'answer': [{
            'valueInteger': 2
        }]
    },
    {
        'linkId': 'MMSE-12',
        'text': '請從100開始連續減7,一直減7直到我說停為止。(每減對一次得一分)',
        'answer': [{
            'valueInteger': 2
        }]
    },
    {
        'linkId': 'MMSE-13',
        'text': '藍色',
        'answer': [{
            'valueInteger': 0
        }]
    },
    {
        'linkId': 'MMSE-14',
        'text': '悲傷',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-15',
        'text': '火車',
        'answer': [{
            'valueInteger': 0
        }]
    },
    {
        'linkId': 'MMSE-16',
        'text': '(拿出手錶)這是什麼?',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-17',
        'text': '(拿出鉛筆)這是什麼?',
        'answer': [{
            'valueInteger': 0
        }]
    },
    {
        'linkId': 'MMSE-18',
        'text': '請跟我唸一句話『白紙真正寫黑字』',
        'answer': [{
            'valueInteger': 0
        }]
    },
    {
        'linkId': 'MMSE-19',
        'text': '請唸一遍並做做看『請閉上眼睛』',
        'answer': [{
            'valueInteger': 1
        }]
    },
    {
        'linkId': 'MMSE-20',
        'text': '請用左/右手(非利手)拿這張紙(三步驟指令,每對一步驟得一分)',
        'answer': [{
            'valueInteger': 0
        }]
    },
    {
        'linkId': 'MMSE-21',
        'text': '請在紙上寫一句語意完整的句子。(含主詞動詞且語意完整的句子)',
        'answer': [{
            'valueInteger': 0
        }]
    },
    {
        'linkId': 'MMSE-22',
        'text': '這裡有一個圖形,請在旁邊畫出一個相同的圖形。(兩五邊形,交一四邊形,有兩交點,則給分)',
        'answer': [{
            'valueInteger': 0
        }]
    }]]
    cdr_items = [
        [{
            'linkId': 'CDR-1',
            'text': '記憶力',
            'answer': [{
                'valueInteger': 3
            }]
        },
        {
            'linkId': 'CDR-2',
            'text': '定向感',
            'answer': [{
                'valueInteger': 3
            }]
        },
        {
            'linkId': 'CDR-3',
            'text': '解決問題能力',
            'answer': [{
                'valueInteger': 3
            }]
        },
        {
            'linkId': 'CDR-4',
            'text': '社區活動能力',
            'answer': [{
                'valueInteger': 3
            }]
        },
        {
            'linkId': 'CDR-5',
            'text': '家居嗜好',
            'answer': [{
                'valueInteger': 3
            }]
        },
        {
            'linkId': 'CDR-6',
            'text': '自我照料',
            'answer': [{
                'valueInteger': 2
            }]
        },
        {
            'linkId': 'CDR-Total',
            'text': '目前的失智期',
            'answer': [{
                'valueInteger': 2
            }]
        }],
        [{
            'linkId': 'CDR-1',
            'text': '記憶力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-2',
            'text': '定向感',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-3',
            'text': '解決問題能力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-4',
            'text': '社區活動能力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-5',
            'text': '家居嗜好',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-6',
            'text': '自我照料',
            'answer': [{
                'valueInteger': 0
            }]
        },
        {
            'linkId': 'CDR-Total',
            'text': '目前的失智期',
            'answer': [{
                'valueInteger': 1
            }]
        }],
        [{
            'linkId': 'CDR-1',
            'text': '記憶力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-2',
            'text': '定向感',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-3',
            'text': '解決問題能力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-4',
            'text': '社區活動能力',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-5',
            'text': '家居嗜好',
            'answer': [{
                'valueInteger': 1
            }]
        },
        {
            'linkId': 'CDR-6',
            'text': '自我照料',
            'answer': [{
                'valueInteger': 0
            }]
        },
        {
            'linkId': 'CDR-Total',
            'text': '目前的失智期',
            'answer': [{
                'valueInteger': 1
            }]
        }]
    ]

    expected = dict(expected_payload_template)

    expected['extension'] = extensions[0]
    expected['authored'] = authored_lists[0]
    expected['item'] = cdr_items[0]
    expected['meta']['profile'] = profile_urls[0]
    expected['questionnaire'] = questionnaires[0]

    payload = dict(payload_template)

    payload['profile_urls'] = profile_urls[0]
    payload['extensions'] = extensions[0]
    payload['questionnaires'] = questionnaires[0]
    payload['status'] = 'completed'
    payload['subject'] = {
        'reference': 'Patient/ltc-patient-chen-ming-hui'
    }
    payload['authored_lists'] = authored_lists[0]
    payload['author'] = {
        'reference': 'Practitioner/ltc-practitioner-physician-aa12-example'
    }
    payload['source'] = {
        'reference': 'Patient/ltc-patient-chen-ming-hui'
    }
    payload['items'] = cdr_items[0]

    json_dict = {}
    json_dict['payload'] = payload
    response = client.post('/api/v1/ltc_tw_2025_questionnaire_response', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert len(response_json['data'][0]['extension']) == 1

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == expected
