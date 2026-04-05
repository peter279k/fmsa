import hashlib
import secrets
from app.modules.BaseConverter import BaseConverter


class LocationLtcConverter(BaseConverter):
    def convert(self, original_data: list):
        converted_result = []
        payload_template = {
            'resourceType': 'Location',
            'id': None,
            'status': 'active',
            'name': '',
            'description': '',
            'mode': 'instance',
            'type': [{
                'coding': [{
                    'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode',
                    'code': 'PTRES',
                    'display': 'Patient\'s Residence',
                 }],
            }],
            'address': {
                'use': 'work',
                'type': 'physical',
                'text': '',
            },
            'position': {
                'longitude': 0,
                'latitude': 0,
                'altitude': 25.5
            }
        }

        address_number = 123
        for location_info in original_data:
            payload = dict(payload_template)
            location_id = secrets.token_urlsafe(5)
            location_id = hashlib.sha3_224(location_id.encode('utf-8')).hexdigest()
            payload['id'] = location_id
            payload['name'] = location_info['name']
            payload['description'] = location_info['location_name']
            payload['address']['text'] = f'新北市中和區安康路二段{address_number}號'
            payload['position']['longitude'] = location_info['longitude']
            payload['position']['latitude'] = location_info['latitude']

            converted_result += payload,
            address_number += 1

        return converted_result
