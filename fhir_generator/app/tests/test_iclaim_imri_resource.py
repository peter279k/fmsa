import json
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_create_track8_2024_practitioner_role_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/practitionerrole-iclaim'],
            'practitioner': {
                'reference': 'Practitioner/Practitioner-Chen',
                'display': '陳健骨'
            },
            'code': [{
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '405279007',
                    'display' : 'Attending physician (occupation)'
                }]
            }],
        },
    }

    with open('/app/app/tests/expected_track8_2024_practitioner_role.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_practitioner_role', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_practitioner_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/practitioner-iclaim'],
            'identifiers': [{
                'use': 'official',
                'type': {
                    'coding': [{
                        'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code' : 'MD'
                    }]
                },
                'system' : 'https://www.cgh.org.tw',
                'value' : '031932'
            }],
            'name': [{
                'use': 'official',
                'text': '陳健骨'
            }]
        },
    }

    with open('/app/app/tests/expected_track8_2024_practitioner.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_practitioner', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_practitioner_resource_on_name_only():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/practitioner-imri'],
            'name': [{
                'use': 'official',
                'text': '劉伊詩',
            }]
        },
    }

    with open('/app/app/tests/expected_track8_2024_practitioner_imri_min.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_practitioner?type=imri-min', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_patient_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/patient-iclaim'],
            'extension': [{
                'url': 'https://claim.cgh.org.tw/iclaim/StructureDefinition/cathay-occupation',
                'valueCodeableConcept': {
                    'coding': [{
                        'system': 'https://claim.cgh.org.tw/iclaim/CodeSystem/lia-roc-occupation-values',
                        'code': '00010010'
                    }]
                }
            }],
            'identifiers': [{
                'use' : 'official',
                'type' : {
                    'coding' : [{
                        'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code' : 'NNxxx',
                        '_code' : {
                            'extension' : [{
                                'extension' : [{
                                    'url' : 'suffix',
                                    'valueString' : 'TWN'
                                },
                                {
                                    'url' : 'valueSet',
                                    'valueCanonical' : 'http://hl7.org/fhir/ValueSet/iso3166-1-3'
                                }],
                                'url' : 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/identifier-suffix'
                            }]
                        }
                    }]
                },
                'system' : 'http://www.moi.gov.tw',
                'value' : 'C251401029'
            },
            {
                'use' : 'official',
                'type' : {
                    'coding' : [{
                        'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code' : 'MR'
                    }]
                },
                'system' : 'https://www.cgh.org.tw',
                'value' : 'ADCM9487'
            }],
            'name_use': 'usual',
            'name_text': '郝美麗',
            'gender': 'female',
            'birth_date' : '1990-04-22',
            'address': [{
                'extension' : [{
                    'url' : 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/tw-number',
                    'valueString' : '365號'
                }],
                'text' : '台北市北投區明德路365號',
                'line' : ['明德路'],
                'city' : '北投區',
                'district' : '台北市',
                'country' : 'TW'
            }]
        },
    }

    with open('/app/app/tests/expected_track8_2024_patient.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_patient', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_patient_imri_min_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/patient-imri'],
            'identifiers': [{
                'use' : 'official',
                'type' : {
                    'coding' : [{
                        'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code' : 'NNxxx',
                        '_code' : {
                            'extension' : [{
                                'extension' : [{
                                    'url' : 'suffix',
                                    'valueString' : 'TWN'
                                },
                                {
                                    'url' : 'valueSet',
                                    'valueCanonical' : 'http://hl7.org/fhir/ValueSet/iso3166-1-3'
                                }],
                                'url' : 'https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/identifier-suffix'
                            }]
                        }
                    }]
                },
                'system' : 'http://www.moi.gov.tw',
                'value' : 'A123456789'
            },
            {
                'use' : 'official',
                'type' : {
                    'coding' : [{
                        'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code' : 'MR'
                    }]
                },
                'system' : 'https://www.cgh.org.tw',
                'value' : '70892114'
            }],
            'name_use': 'usual',
            'name_text': '安格斯',
            'gender': 'male',
            'birth_date' : '2000-02-02',
        },
    }

    with open('/app/app/tests/expected_track8_2024_patient_imri_min.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_patient?type=imri-min', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_organization_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Organization-hosp-twcore'],
            'identifiers': [{
                'use': 'official',
                'type': {
                    'coding': [{
                        'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                        'code': 'PRN'
                    }]
                },
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/organization-identifier-tw',
                'value': '1101020018'
            }],
            'type_coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
                'code': 'prov'
            }],
            'name': '國泰醫療財團法人國泰綜合醫院',
        },
    }

    with open('/app/app/tests/expected_track8_2024_organization_min.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_organization', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_observation_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/observation-iclaim'],
            'identifiers': [{
                'system' : 'https://www.cgh.org.tw',
                'value' : '096H004'
            }],
            'status': 'final',
            'category_coding': [{
                'system' : 'http://terminology.hl7.org/CodeSystem/observation-category',
                'code' : 'laboratory'
            }],
            'code_coding': [{
                'system' : 'http://loinc.org',
                'code' : '100856-4',
                'display' : 'CD3+CD4+ (T4 helper) cells/100 cells in Blood mononuclear cells'
            }],
            'subject': {
                'reference': 'Patient/Patient-C1',
            },
            'effective_datetime': '2023-08-07',
            'issued': '2023-08-07T17:00:14+08:00',
            'performer': [
                {
                    'reference' : 'PractitionerRole/PractitionerRole-tech'
                },
                {
                    'reference' : 'PractitionerRole/PractitionerRole-rep'
                },
            ],
            'value_quantity':  {
                'value' : 4000,
                'unit' : '/uL',
                'system' : 'http://unitsofmeasure.org'
            },
            'note': [{
                'text' : '無'
            }],
            'interpretation': [{
                'coding' : [{
                    'system' : 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation',
                    'code' : '<'
                }]
            }],
            'body_site_coding': [{
                'system' : 'http://snomed.info/sct',
                'code' : '9736006'
            }],
            'reference_range': [{
                'low' : {
                    'value' : 4500
                },
                'high' : {
                    'value' : 10000
                }
            }],
        },
    }

    with open('/app/app/tests/expected_track8_2024_observation_c1.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_observation', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_observation_cancer_staging_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/observation-cancerstaging-imri'],
            'status': 'final',
            'category_coding': [{
                'system' : 'http://loinc.org',
                'code' : '22037-6',
                'display' : 'Staging Cancer Narrative'
            }],
            'code_coding': [{
                'system' : 'http://snomed.info/sct',
                'code' : '399537006',
                'display' : 'Clinical TNM stage grouping'
            }],
            'subject': {
                'reference': 'Patient/Patient-min',
            },
            'effective_datetime': '2024-04-01',
            'performer': [{
                'reference' : 'Practitioner/Practitioner-min'
            }],
            'value_codeable_concept': {
                'coding' : [{
                    'system' : 'http://snomed.info/sct',
                    'code' : '1222806003',
                    'display' : 'American Joint Committee on Cancer stage IIIC (qualifier value)'
                }],
            }
        },
    }

    with open('/app/app/tests/expected_track8_2024_observation_cancer_staging.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_observation?type=imri-cancer-staging', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_encounter_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/encounter-iclaim'],
            'extension': [{
                'url' : 'https://claim.cgh.org.tw/iclaim/StructureDefinition/cathay-medicalidentity',
                'valueCodeableConcept' : {
                    'coding' : [{
                        'system' : 'http://terminology.hl7.org/CodeSystem/coverage-selfpay',
                        'code' : 'pay'
                    }]
                }
            }],
            'identifiers': [{
                'system' : 'https://www.cgh.org.tw',
                'value' : '1286481'
            }],
            'status': 'finished',
            'fixture_class': {
                'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
                'code' : 'AMB'
            },
            'service_type_coding':  [{
                'system' : 'https://claim.cgh.org.tw/iclaim/CodeSystem/nhi-department-values',
                'code' : '06',
                'display' : '骨科'
            }],
            'subject': {
                'reference': 'Patient/Patient-C1'
            },
            'participant_individual': {
                'reference' : 'PractitionerRole/PractitionerRole-rec'
            },
            'period': {
                'start' : '2023-08-07T17:00:14-05:00',
                'end' : '2023-08-07T18:00:14-05:00'
            },
            'length':  {
                'value' : 1,
                'unit' : 'days',
                'system' : 'http://unitsofmeasure.org',
                'code' : 'd'
            },
        },
    }

    with open('/app/app/tests/expected_track8_2024_encounter_c1.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_encounter', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_encounter_imri_min_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/encounter-imri'],
            'status': 'finished',
            'fixture_class': {
                'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
                'code' : 'PRENC'
            },
            'service_type_coding': [{
                'system' : 'http://snomed.info/sct',
                'code' : '408464004',
                'display' : 'Colorectal Surgery'
            }],
            'subject': {
                'reference': 'Patient/Patient-min'
            },
            'participant_individual': {
                'reference' : 'Practitioner/Practitioner-min'
            },
            'period': {
                'start' : '2023-09-06T17:00:14+08:00',
                'end' : '2023-09-12T18:00:14+08:00'
            },
            'hospitalization': {
                'destination' : {
                    'reference' : 'Location/Location-min'
                },
                'dischargeDisposition' : {
                    'text' : '改門診治療'
                }
            },
        },
    }

    with open('/app/app/tests/expected_track8_2024_encounter_min.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_encounter?type=imri-min', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_diagnostic_report_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/diagnosticreport-iclaim'],
            'status': 'final',
            'fixture_class': {
                'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
                'code' : 'AMB'
            },
            'code_coding': [{
                'system' : 'http://loinc.org',
                'code' : '100537-0'
            }],
            'subject': {
                'reference': 'Patient/Patient-C1'
            },
            'result': [{
                'reference': 'Observation/Observation-C1'
            }],
        },
    }

    with open('/app/app/tests/expected_track8_2024_diagnostic_report_c1.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_diagnostic_report', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_coverage_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/coverage-iclaim'],
            'status': 'active',
            'beneficiary': {
                'reference' : 'Patient/Patient-C1'
            },
            'payor': [{
                'reference' : 'Organization/Organization-cathay'
            }]
        },
    }

    with open('/app/app/tests/expected_track8_2024_coverage_c1.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_coverage', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_condition_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/condition-iclaim'],
            'identifier': [{
                'value': '1080108642',
            }],
            'clinical_status_coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/condition-clinical',
                'code': 'remission',
            }],
            'category_coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/condition-category',
                'code': 'encounter-diagnosis'
            }],
            'code_coding': [{
                'system': 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-9-cm-2001-tw',
                'code': '842.19',
                'display': '手其他部位扭傷及拉傷',
            }],
            'subject': {
                'reference': 'Patient/Patient-C1'
            },
            'encounter': {
                'reference': 'Encounter/Encounter-C1',
            },
            'recorded_date': '2023-08-07',
            'recorder': {
                'reference': 'PractitionerRole/PractitionerRole-pri',
            },
            'asserter': {
                'reference': 'PractitionerRole/PractitionerRole-res'
            },
            'stage': [{
                'assessment' : [{
                    'reference' : 'DiagnosticReport/DiagnosticReport-C1'
                }]
            }],
            'note': [{
                'text': '手扭傷後,關節局部腫脹,關節彎曲受限,伸不直或彎曲不了',
            }],
        },
    }

    with open('/app/app/tests/expected_track8_2024_condition_c1.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_condition', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_condition_chief_comp_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/conditionchiefcomplaint-imri'],
            'clinical_status_coding': [{
                'system' : 'http://terminology.hl7.org/CodeSystem/condition-clinical',
                'code' : 'active',
                'display' : 'Active'
            }],
            'category_coding': [{
                'system' : 'http://loinc.org',
                'code' : '10154-3',
                'display' : 'Chief complaint Narrative - Reported'
            }],
            'code_coding': [{
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-cm-2021-tw',
                'code' : 'K62.5',
                'display' : '肛門及直腸出血'
            }],
            'code_text': '肛門及直腸出血',
            'subject': {
                'reference': 'Patient/Patient-min'
            },
            'encounter': {
                'reference': 'Encounter/Encounter-min',
            },
            'note': [{
                'text' : 'Anal pain with anal bleeding for few days'
            }],
        },
    }

    with open('/app/app/tests/expected_track8_2024_condition_chief.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_condition?type=ConditionChiefComplaint-min', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_composition_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/composition-iclaim'],
            'identifier': {
                'system' : 'https://www.cgh.org.tw',
                'value' : 'A0001'
            },
            'status': 'final',
            'type_coding': [{
                'system' : 'http://loinc.org',
                'code' : '64291-8'
            }],
            'subject': {
                'reference' : 'Patient/Patient-C1'
            },
            'date': '2023-08-21T14:30:00+08:00',
            'author': [{
                'reference' : 'Organization/Organization-min'
            }],
            'title': '理賠用收據-診斷證明-檢驗紀錄',
            'section_title': '理賠用收據-診斷證明-檢驗紀錄',
            'section_code': {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '64291-8'
                }]
            },
            'section_entry': [{
                'reference' : 'Claim/Claim-C1'
            },
            {
                'reference' : 'Coverage/Coverage-C1'
            },
            {
                'reference' : 'Organization/Organization-cathay'
            },
            {
                'reference' : 'Condition/Condition-C1'
            },
            {
                'reference' : 'DiagnosticReport/DiagnosticReport-C1'
            },
            {
                'reference' : 'Encounter/Encounter-C1'
            },
            {
                'reference' : 'Practitioner/Practitioner-Chen'
            },
            {
                'reference' : 'Practitioner/Practitioner-Ciou'
            },
            {
                'reference' : 'Practitioner/Practitioner-Wang1'
            },
            {
                'reference' : 'Observation/Observation-C1'
            }]
        },
    }

    with open('/app/app/tests/expected_track8_2024_composition_c1.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_composition', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_composition_discharge_summary_min_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/composition-dischargesummary-imri'],
            'status': 'final',
            'type_coding': [{
                'system' : 'http://loinc.org',
                'code' : '18842-5',
                'display' : 'Discharge summary'
            }],
            'subject': {
                'reference' : 'Patient/Patient-min'
            },
            'encounter': {
                'reference' : 'Encounter/Encounter-min'
            },
            'date': '2024-05-12T14:30:00+08:00',
            'author': [
                {
                    'reference' : 'Organization/OrganizationHosp-min'
                },
                {
                    'reference' : 'Practitioner/Practitioner-min'
                }
            ],
            'title': '出院病歷摘要',
            'section': [{
            'title' : '住院臆斷',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '46241-6',
                    'display' : 'Hospital admission diagnosis Narrative - Reported'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationImpression-min'
            }]
        },
        {
            'title' : '出院診斷',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '11535-2',
                    'display' : 'Hospital discharge Dx Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionDischargeDiagnosis-min'
            }]
        },
        {
            'title' : '癌症期別',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '22037-6',
                    'display' : 'Staging Cancer Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationCancerStaging-min'
            }]
        },
        {
            'title' : '主訴',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '10154-3',
                    'display' : 'Chief complaint Narrative - Reported'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionChiefComplaint-min'
            }]
        },
        {
            'title' : '病史',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '10164-2',
                    'display' : 'History of Present illness Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionPresentIllness-min'
            }]
        },
        {
            'title' : '理學檢查發現',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '29545-1',
                    'display' : 'Physical findings Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationPhysicalExamination-min'
            }]
        },
        {
            'title' : '檢驗與特殊檢查',
                'code' : {
                    'coding' : [{
                        'system' : 'http://loinc.org',
                        'code' : '30954-2',
                        'display' : 'Relevant diagnostic tests/laboratory data Narrative'
                    }]
                },
            'entry' : [{
                    'reference' : 'Observation/ObservationLaboratory-min'
                },
                {
                    'reference' : 'Observation/ObservationLaboratory-lab'
                }]
        },
        {
            'title' : '醫療影像檢查',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '18748-4',
                    'display' : 'Diagnostic imaging study'
                }]
            },
            'entry' : [{
                'reference' : 'ImagingStudy/ImagingStudy-min'
            }]
        },
        {
            'title' : '病理報告',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '22034-3',
                    'display' : 'Pathology report Cancer Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Observation/ObservationPathologyReport-min'
            }]
        },
        {
            'title' : '手術日期及方法',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '8724-7',
                    'display' : 'Surgical operation note description Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Procedure/Procedure-min'
            }]
        },
        {
            'title' : '住院治療經過',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '8648-8',
                    'display' : 'Hospital course Narrative'
                }]
            },
            'entry' : [{
                'reference' : 'Procedure/ProcedureHospitalCourse-min'
            },
            {
                'reference' : 'Location/Location-min'
            }]
        },
        {
            'title' : '合併症與併發症',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '55109-3',
                    'display' : 'Complications Document'
                }]
            },
            'entry' : [{
                'reference' : 'Condition/ConditionComorbiditiesandComplications-min'
            }]
        },
        {
            'title' : '出院指示',
            'code' : {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '8653-8',
                    'display' : 'Hospital Discharge instructions'
                }]
            },
            'entry' : [{
                'reference' : 'CarePlan/CarePlan-min'
            },
            {
                'reference' : 'MedicationRequest/MedicationRequest-min'
            }]
        }]
        },
    }

    with open('/app/app/tests/expected_track8_2024_composition_discharge_summary.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_composition?type=discharge-summary-min', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_claim_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://claim.cgh.org.tw/iclaim/StructureDefinition/claim-iclaim'],
            'identifier': [{
                'system' : 'https://www.cgh.org.tw',
                'value' : 'A0001'
            }],
            'status': 'active',
            'type_coding': [{
                'system' : 'http://terminology.hl7.org/CodeSystem/claim-type',
                'code' : 'institutional'
            }],
            'patient': {
                'reference' : 'Patient/Patient-C1'
            },
            'created': '2023-08-07',
            'provider': {
                'reference' : 'Organization/Organization-min'
            },
            'priority_coding': [{
                'system' : 'http://terminology.hl7.org/CodeSystem/processpriority',
                'code' : 'stat'
            }],
            'diagnosis': [{
                'sequence' : 1,
                'diagnosisReference' : {
                    'reference' : 'Condition/Condition-C1'
                }
            }],
            'insurance': [{
                'sequence' : 1,
                'focal' : True,
                'coverage' : {
                    'reference' : 'Coverage/Coverage-C1'
                }
            }],
            'item': [{
                'sequence' : 1,
                'category' : {
                    'coding' : [{
                        'system' : 'http://hl7.org/fhir/invoice-priceComponentType',
                        'code' : 'base'
                    }]
                },
                'productOrService' : {
                    'coding' : [{
                        'system' : 'https://claim.cgh.org.tw/iclaim/CodeSystem/cathay-chargeitemcode-values',
                        'code' : 'REGISTRATION'
                    }]
                },
                'modifier' : [{
                    'coding' : [{
                        'system' : 'http://terminology.hl7.org/CodeSystem/coverage-selfpay',
                        'code' : 'pay'
                    }]
                }],
                'servicedDate' : '2023-08-07',
                'net' : {
                    'value' : 150
                }
            },
            {
                'sequence' : 2,
                'productOrService' : {
                    'coding' : [{
                        'system' : 'https://claim.cgh.org.tw/iclaim/CodeSystem/cathay-chargeitemcode-values',
                        'code' : 'REGISTRATION'
                    }]
                },
                'modifier' : [{
                    'coding' : [{
                        'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
                        'code' : 'PUBLICPOL'
                    }]
                }],
                'servicedDate' : '2023-08-07',
                'net' : {
                    'value' : 580
                }
            }],
            'total': {
                'value' : 150
            },
        },
    }

    with open('/app/app/tests/expected_track8_2024_claim_c1.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_claim', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_procedure_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/procedure-imri'],
            'status': 'completed',
            'category': {
                'coding' : [{
                    'system' : 'http://loinc.org',
                    'code' : '8724-7',
                    'display' : 'Surgical operation note description Narrative'
                }]
            },
            'code_coding': [{
                'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/icd-10-pcs-2021-tw',
                'code' : '06BY0ZC',
                'display' : '開放性痔靜脈叢部分切除術'
            }],
            'code_text': '開放性痔靜脈叢部分切除術',
            'subject': {
                'reference': 'Patient/Patient-min'
            },
            'encounter': {
                'reference' : 'Encounter/Encounter-min'
            },
            'performed_date_time': '2023-09-08T11:25:11+08:00',
        },
    }

    with open('/app/app/tests/expected_track8_2024_procedure_min.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_procedure', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_medication_request_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/medicationrequest-imri'],
            'status': 'active',
            'intent': 'proposal',
            'medication_codeable_concept': {
                'coding' : [{
                    'system' : 'https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-nhi-tw',
                    'code' : 'A003092100',
                    'display' : 'ASPIRIN TABLETS 500MG "S.Y."'
                }]
            },
            'subject': {
                'reference': 'Patient/Patient-min'
            },
            'encounter': {
                'reference': 'Encounter/Encounter-min'
            },
            'requester': {
                'reference': 'Practitioner/Practitioner-min'
            },
            'performer': {
                'reference' : 'Practitioner/Practitioner-min'
            },
            'based_on': [{
                'reference' : 'CarePlan/CarePlan-min'
            }],
        },
    }

    with open('/app/app/tests/expected_track8_2024_medication_request_min.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_medication_request', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_location_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/location-imri'],
            'identifier': [{
                'value' : '4012S'
            }],
            'name': '病床',
        },
    }

    with open('/app/app/tests/expected_track8_2024_location_min.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_location', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_imaging_study_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/imagingstudy-imri'],
            'status': 'available',
            'subject': {
                'reference': 'Patient/Patient-min'
            },
            'encounter': {
                'reference': 'Encounter/Encounter-min'
            },
            'started': '2023-09-07T11:01:20+03:00',
            'interpreter': [{
                'reference' : 'Practitioner/Practitioner-min'
            }],
            'description': 'No significant roentgenological abnormality is observed.',
        },
    }

    with open('/app/app/tests/expected_track8_2024_imaging_study.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_imaging_study', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_document_reference_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/DocumentReference-twcore'],
            'status': 'current',
            'subject': {
                'reference': 'Patient/Patient-min'
            },
            'content': [{
                'attachment' : {
                    'contentType' : 'image/png',
                    'url' : 'https://telegraph-image-55i.pages.dev/file/3830a304a2eb70419c80a.png',
                    'title' : 'gallbladder polyp'
                }
            }]
        },
    }

    with open('/app/app/tests/expected_track8_2024_document_reference.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_document_reference', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)

def test_create_track8_2024_care_plan_resource():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    payload = {
        'payload': {
            'profile_urls': ['https://hitstdio.ntunhs.edu.tw/imri/StructureDefinition/careplan-imri'],
            'status': 'completed',
            'intent': 'proposal',
            'description': '出院指示',
            'subject': {
                'reference': 'Patient/Patient-min'
            },
            'encounter': {
                'reference': 'Encounter/Encounter-min',
            },
            'activity': [{
                'reference' : {
                    'reference' : 'MedicationRequest/MedicationRequest-min'
                }
            }],
        },
    }

    with open('/app/app/tests/expected_track8_2024_care_plan_imri_min.json', 'r', encoding='utf-8') as f:
        expected_json_str = f.read()

    json_dict = payload
    response = client.post('/api/v1/track8_2024_care_plan', headers=headers, json=json_dict)

    response_json = response.json()
    del response_json['data'][0]['id']

    assert response.status_code == 200
    assert len(response_json['data']) == 1
    assert response_json['data'][0] == json.loads(expected_json_str)
