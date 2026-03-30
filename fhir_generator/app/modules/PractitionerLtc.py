import hashlib
import secrets
from fhir_data_generator import PractitionerLtc as Practitioner


class PractitionerLtc:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.practitioner_payload = item_dict['payload']
        self.resource = resource
        self.type = item_dict['type']

    def generate_practitioner_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        practitioner_class = Practitioner(resource_id)

        if self.type == 'aa12':
            practitioner_class.set_profile_urls(self.practitioner_payload['profile_urls'])

            practitioner_class.set_identifiers(self.practitioner_payload['identifiers'])

            practitioner_class.set_name(self.practitioner_payload['name'])

            practitioner_class.set_telecom(self.practitioner_payload['telecom'])

            practitioner_class.set_address(self.practitioner_payload['address'])

            practitioner_class.set_gender(self.practitioner_payload['gender'])

            practitioner_class.set_birth_date(self.practitioner_payload['birth_date'])

            practitioner_class.set_qualification(self.practitioner_payload['qualification'])

        if self.type == 'nurse':
            practitioner_class.set_profile_urls(self.practitioner_payload['profile_urls'])

            practitioner_class.set_identifiers(self.practitioner_payload['identifiers'])

            practitioner_class.set_active(self.practitioner_payload['active'])

            practitioner_class.set_name(self.practitioner_payload['name'])

            practitioner_class.set_telecom(self.practitioner_payload['telecom'])

            practitioner_class.set_gender(self.practitioner_payload['gender'])

            practitioner_class.set_qualification(self.practitioner_payload['qualification'])

        if self.type == 'ltc':
            practitioner_class.set_profile_urls(self.practitioner_payload['profile_urls'])

            practitioner_class.set_identifiers(self.practitioner_payload['identifiers'])

            practitioner_class.set_active(self.practitioner_payload['active'])

            practitioner_class.set_name(self.practitioner_payload['name'])

            practitioner_class.set_telecom(self.practitioner_payload['telecom'])

            practitioner_class.set_address(self.practitioner_payload['address'])

            practitioner_class.set_gender(self.practitioner_payload['gender'])

            practitioner_class.set_birth_date(self.practitioner_payload['birth_date'])


        practitioner_class.create()

        return practitioner_class.payload_template
