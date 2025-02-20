import hashlib
from fhir_data_generator import PatientEX


class GoldenSmartHomeConverter:
    def convert(self, original_data: list):
        user_ids = []
        user_id_info = {}
        mapping_gender = {
            '男': 'male',
            '女': 'female',
        }
        patient_infos = []
        for record in original_data:
            if record['user_id'] not in user_ids:
                user_ids += record['user_id'],
                user_id_info[record['user_id']] = {
                    'birth_year': record['birth_year'],
                    'user_id': record['user_id'],
                    'gender': mapping_gender[record['gender']],
                    'identifier_system': 'https://www.goldensmarthome.com.tw',
                    'identifier_value': record['user_id'],
                }

        for user_id in user_ids:
            patient_class = PatientEX(hashlib.sha3_224(user_id.encode('utf-8')).hexdigest())
            patient_class.set_identifiers([{
                'system': user_id_info[user_id]['identifier_system'],
                'value': user_id_info[user_id]['identifier_value'],
            }])
            patient_class.set_name_text(user_id_info[user_id]['user_id'])
            patient_class.set_gender(user_id_info[user_id]['gender'])
            patient_class.set_birth_date(user_id_info[user_id]['birth_year'])
            patient_class.create()

            del patient_class.payload_template['extension']
            del patient_class.payload_template['meta']

            patient_infos += patient_class.payload_template,

        return patient_infos


