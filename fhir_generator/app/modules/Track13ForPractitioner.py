import hashlib
import secrets
from fhir_data_generator import PhysicalActivityPractitioner as Practitioner


class Track13ForPractitioner:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.practitioner_payload = item_dict['practitioner_payload']
        self.resource = resource

    def generate_practitioner_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        practitioner_class = Practitioner(resource_id)

        profile_urls = self.practitioner_payload['profile_urls']

        practitioner_class.set_profile_urls(profile_urls)

        practitioner_class.set_identifiers(self.practitioner_payload['identifiers'])

        practitioner_class.set_active(self.practitioner_payload['active'])

        practitioner_class.set_name_text(self.practitioner_payload['name_text'])

        practitioner_class.create()

        return practitioner_class.payload_template
