import hashlib
import secrets
from app.modules.BaseConverter import BaseConverter


class AdverseEventLtcConverter(BaseConverter):
    def convert(self, original_data: list):
        converted_result = []
        payload_template = {
            'resourceType': 'AdverseEvent',
            'id': None,
            'extension': [],
            'identifier': {
                'use': 'official',
                'system': 'http://ltc-ig.fhir.tw/adverse-event',
                'value': 'AE-2024-001'
            },
            'actuality': 'actual',
            'event': {
                'text': '',
            },
            'subject': {
                'reference': 'Patient/ltc-patient-chen-ming-hui'
            },
            'date': '',
            'detected': '',
            'recordedDate': '',
            'location': {
                'reference': 'Location/ltc-location-example'
            },
            'seriousness': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/adverse-event-seriousness',
                    'code': 'serious',
                    'display': 'Serious'
                }]
            },
            'severity': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/adverse-event-severity',
                    'code': 'moderate',
                    'display': 'Moderate'
                }]
            },
            'outcome': {
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/adverse-event-outcome',
                    'code': 'recovering',
                    'display': 'Recovering'
                }]
            },
            'recorder': {
                'reference': 'Practitioner/ltc-practitioner-example'
            },
        }

        for adverse_event in original_data:
            payload = dict(payload_template)

            adverse_event_id = secrets.token_urlsafe(5)
            adverse_event_id = hashlib.sha3_224(adverse_event_id.encode('utf-8')).hexdigest()
            payload['id'] = adverse_event_id

            extension = list(payload['extension'])
            extension = [{
                'extension': [],
                'url': 'http://ltc-ig.fhir.tw/StructureDefinition/Ext-TW-LTC-AdverseEvent-Description'
            }]
            extension[0]['extension'] += {
                'url': 'textType',
                'valueCodeableConcept': {
                    'coding': [{
                        'system': 'http://ltc-ig.fhir.tw/CodeSystem/cs-tw-ltc-incident-texttype',
                        'code': 'desc',
                        'display': '事件描述'
                    }]
                }
            },
            extension += {
                'url': 'text',
                'valueString': adverse_event['事件類型描述'],
            },
            payload['extension'][0]['extension'] = list(extension)

            event = dict(payload['event'])
            event['text'] = adverse_event['結果狀況']
            payload['event'] = dict(event)

            iso8601_datetime = self.convert_iso_datetime(adverse_event['發生時間'])

            payload['date'] = iso8601_datetime
            payload['detected'] = iso8601_datetime
            payload['recordedDate'] = iso8601_datetime

            converted_result += payload,

        return converted_result

    def convert_iso_datetime(self, event_datetime):
        datetime = event_datetime.split(' ')
        date = datetime[0]
        time = datetime[1]

        return f'{date}T{time}+08:00'
