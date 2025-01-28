import hashlib
import secrets
from fhir_data_generator import TWCoreOrganization as Organization


class Track8ForOrganization:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.resource = resource
        self.organization_payload = item_dict['payload']

    def generate_organization_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        organization_class = Organization(resource_id)

        profile_urls = self.organization_payload['profile_urls']
        organization_class.set_profile_urls(profile_urls)

        organization_class.set_identifiers(self.organization_payload['identifiers'])

        organization_class.set_type_coding(self.organization_payload['type_coding'])

        organization_class.set_name(self.organization_payload['name'])

        organization_class.create()

        return organization_class.payload_template
