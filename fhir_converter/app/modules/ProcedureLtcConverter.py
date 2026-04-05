import hashlib
import secrets
from app.modules.BaseConverter import BaseConverter


class ProcedureLtcConverter(BaseConverter):
    def convert(self, original_data: list):
        converted_result = []
        payload_template = {
            'resourceType': 'Procedure',
            'id': None,
            'status': 'completed',
            'code': {},
            'subject': {
                'reference': 'Patient/ltc-patient-chen-ming-hui'
            },
            'performedDateTime': '',
            'performer': [{
                'actor': {
                    'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
                }
            }],
            'note': [],
        }

        for procedure in original_data:
            payload = dict(payload_template)
            procedure_id = secrets.token_urlsafe(5)
            procedure_id = hashlib.sha3_224(procedure_id.encode('utf-8')).hexdigest()

            payload['id'] = procedure_id

            code = dict(payload['code'])
            code = {
                'coding' : self.convert_care_code(procedure['照護項目']),
                'text' : procedure['照護項目'],
            }
            payload['code'] = code

            performed_datetime = procedure['日期'] + ' ' + procedure['時間']
            performed_datetime = self.convert_to_iso_datetime(performed_datetime)
            payload['performedDateTime'] = performed_datetime

            note = list(payload['note'])
            note += {
                'time': performed_datetime,
                'text': procedure['案主狀況'],
            },
            payload['note'] = note

            converted_result += payload,

        return converted_result

    def convert_to_iso_datetime(self, performed_datetime: str):
        performed_datetime = performed_datetime.replace('/', '-').split(' ')
        date = performed_datetime[0]
        time = performed_datetime[1]

        return f'{date}T{time}+08:00'

    def convert_care_code(self, care_item: str):
        care_mapping_table = {
            '進食協助': [{
                'system': 'http://snomed.info/sct',
                'code': '226010006',
                'display': 'Assisting with eating and drinking'
            }],
            '床上移動協助': [{
                'system': 'http://snomed.info/sct',
                'code': '713138001',
                'display': 'Assistance with mobility in bed'
            }],
            '如廁協助': [{
              'system': 'http://snomed.info/sct',
                'code': '223454002',
                'display': 'Escorting subject to toilet'
            }],
            '移位/移動協助': [{
                'system': 'http://snomed.info/sct',
                'code': '710803000',
                'display': 'Assistance with mobility'
            }],
            '更換尿布': [{
                'system': 'http://snomed.info/sct',
                'code': '733923007',
                'display': 'Change of diaper'
            }],
            '沐浴/擦澡': [{
                'system': 'http://snomed.info/sct',
                'code': '60369001',
                'display': 'Bathing patient'
            }],
            '穿衣': [{
                'system': 'http://snomed.info/sct',
                'code': '313332003',
                'display': 'Dressing patient'
            }],
            '陪同到廁所': [{
                'system': 'http://snomed.info/sct',
                'code': '313420001',
                'display': 'Assisting with toileting'
            }],
            '個人衛生協助': [{
                'system': 'http://snomed.info/sct',
                'code': '225964003',
                'display': 'Assisting with personal hygiene'
            }],
        }

        return care_mapping_table.get(care_item)
