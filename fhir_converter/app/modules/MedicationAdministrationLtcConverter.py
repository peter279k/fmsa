import hashlib
import secrets
from app.modules.BaseConverter import BaseConverter


class MedicationAdministrationLtcConverter(BaseConverter):
    def convert(self, original_data: list):
        converted_result = []
        payload_template = {
            'resourceType': 'MedicationAdministration',
            'id': None,
            'status': 'completed',
            'medicationCodeableConcept': {},
            'subject': {
                'reference': 'Patient/ltc-patient-chen-ming-hui'
            },
            'effectiveDateTime': '',
            'performer': [{
                'actor': {
                    'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
                }
            }],
            'note': [],
            'dosage': {},
        }

        for medication in original_data:
            payload = dict(payload_template)
            medication_admin_id = secrets.token_urlsafe(5)
            medication_admin_id = hashlib.sha3_224(medication_admin_id.encode('utf-8')).hexdigest()

            payload['id'] = medication_admin_id

            medication_codeable = dict(payload['medicationCodeableConcept'])
            medication_codeable = self.convert_medication_code(medication['藥品名稱'])
            payload['medicationCodeableConcept'] = medication_codeable

            effective_datetime = medication['開始日期'] + ' ' + '00:00'
            effective_datetime = self.convert_to_iso_datetime(effective_datetime)
            payload['effectiveDateTime'] = effective_datetime

            note = list(payload['note'])
            note += {
                'time': effective_datetime,
                'text': medication['備註'],
            },
            payload['note'] = note

            dosage = dict(payload['dosage'])
            dosage_info = medication['劑量'].split(' ')
            if '%' in dosage_info[0]:
                dosage_info[0] = dosage_info[0][0:-1]
                dosage_info += '%',
            dosage_value = float(dosage_info[0])
            dosage_unit = dosage_info[1]
            dosage = self.convert_dosage_code(medication['用藥途徑'], dosage_value, dosage_unit)
            payload['dosage'] = dosage

            converted_result += payload,

        return converted_result

    def convert_to_iso_datetime(self, effective_datetime: str):
        effective_datetime = effective_datetime.split(' ')
        date = effective_datetime[0]
        time = effective_datetime[1]

        return f'{date}T{time}+08:00'

    def convert_medication_code(self, medication_name: str):
        medication_table = {
            '阿莫西林 Amoxicillin': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '323567000',
                   'display': 'Amoxicillin (as amoxicillin sodium) 500 mg and clavulanic acid (as clavulanate potassium) 100 mg powder for solution for injection vial'
                }],
                'text': 'Amoxicillin (as amoxicillin sodium) 500 mg and clavulanic acid (as clavulanate potassium) 100 mg powder for solution for injection vial'
            },
            '美托洛爾 Metoprolol': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '395483007',
                   'display': 'Metoprolol-containing product in oral dose form'
                }],
                'text': 'Metoprolol-containing product in oral dose form'
            },
            '布地奈德 Budesonide': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '778558005',
                   'display': 'Budesonide only product in nasal dose form'
                }],
                'text': 'Budesonide only product in nasal dose form'
            },
            '二甲雙胍 Metformin': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '1304278000',
                   'display': 'Canagliflozin 50 mg and metformin hydrochloride 850 mg oral tablet'
                }],
                'text': 'Canagliflozin 50 mg and metformin hydrochloride 850 mg oral tablet'
            },
            '地塞米松乳膏 Dexamethasone cream': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '771855007',
                   'display': 'Dexamethasone-containing product in cutaneous dose form'
                }],
                'text': 'Dexamethasone-containing product in cutaneous dose form'
            },
            '胰島素 Insulin glargine': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '126212009',
                   'display': 'Insulin glargine-containing product'
                }],
                'text': 'Insulin glargine-containing product'
            },
            '阿托伐他汀 Atorvastatin': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '108600003',
                   'display': 'Atorvastatin-containing product'
                }],
                'text': 'Atorvastatin-containing product'
            },
            '奧美拉唑 Omeprazole': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '25673006',
                   'display': 'Omeprazole-containing product'
                }],
                'text': 'Omeprazole-containing product'
            },
            '阿斯匹靈 Aspirin': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '7947003',
                   'display': 'Aspirin-containing product'
                }],
                'text': 'Aspirin-containing product'
            },
            '左旋甲狀腺素 Levothyroxine': {
                'coding': [{
                    'system': 'http://snomed.info/sct',
                    'code': '768532006',
                   'display': 'Levothyroxine-containing product'
                }],
                'text': 'Levothyroxine-containing product'
            },
        }

        return medication_table.get(medication_name)

    def convert_dosage_code(self, dosage: str, dose_value: int, dose_unit: str):
        dosage_mapping_table = {
            '口服': {
                'route': {
                    'coding': [{
                        'system': 'http://snomed.info/sct',
                        'code': '26643006',
                        'display': 'Oral route'
                    }],
                    'text': '口服'
                },
                'dose': {
                    'value': dose_value,
                    'unit': dose_unit,
                    'system': 'http://unitsofmeasure.org',
                    'code': dose_unit,
                },
            },
            '吸入': {
                'route': {
                    'coding': [{
                        'system': 'http://snomed.info/sct',
                        'code': '46713006',
                        'display': 'Nasal use'
                    }],
                    'text': '吸入'
                },
                'dose': {
                    'value': dose_value,
                    'unit': dose_unit,
                    'system': 'http://unitsofmeasure.org',
                    'code': dose_unit,
                },
            },
            '外用': {
                'route': {
                    'coding': [{
                        'system': 'http://snomed.info/sct',
                        'code': '6064005',
                        'display': 'Topical route'
                    }],
                    'text': '外用'
                },
                'dose': {
                    'value': dose_value,
                    'unit': dose_unit,
                    'system': 'http://unitsofmeasure.org',
                    'code': dose_unit,
                },
            },
            '注射': {
                'route': {
                    'coding': [{
                        'system': 'http://snomed.info/sct',
                        'code': '34206005',
                        'display': 'SC use'
                    }],
                    'text': '皮下注射'
                },
                'dose': {
                    'value': dose_value,
                    'unit': dose_unit,
                    'system': 'http://unitsofmeasure.org',
                    'code': dose_unit,
                },
            },
        }

        return dosage_mapping_table.get(dosage)
