import hashlib
import secrets
from fhir_data_generator import TWCorePractitionerRole as PractitionerRole


class Track8ForPractitionerRole:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.practitioner_role_payload = item_dict['payload']
        self.resource = resource

    def generate_practitioner_role_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        practitioner_role_class = PractitionerRole(resource_id)

        practitioner_role_class.set_profile_urls(self.practitioner_role_payload['profile_urls'])

        practitioner_role_class.set_practitioner(self.practitioner_role_payload['practitioner'])

        practitioner_role_class.set_code(self.practitioner_role_payload['code'])

        practitioner_role_class.create()

        return practitioner_role_class.payload_template
