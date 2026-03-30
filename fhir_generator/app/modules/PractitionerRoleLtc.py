import hashlib
import secrets
from fhir_data_generator import PractitionerRoleLtc as PractitionerRole


class PractitionerRoleLtc:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.practitioner_role_payload = item_dict['payload']
        self.resource = resource

    def generate_practitioner_role_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        practitioner_role_class = PractitionerRole(resource_id)

        practitioner_role_class.set_profile_urls(self.practitioner_role_payload['profile_urls'])

        practitioner_role_class.set_active(self.practitioner_role_payload['active'])

        practitioner_role_class.set_practitioner(self.practitioner_role_payload['practitioner'])

        practitioner_role_class.set_organization(self.practitioner_role_payload['organization'])

        practitioner_role_class.set_code(self.practitioner_role_payload['code'])

        practitioner_role_class.set_specialty(self.practitioner_role_payload['specialty'])

        practitioner_role_class.set_telecom(self.practitioner_role_payload['telecom'])

        practitioner_role_class.set_available_time(self.practitioner_role_payload['available_time'])

        practitioner_role_class.create()

        return practitioner_role_class.payload_template
