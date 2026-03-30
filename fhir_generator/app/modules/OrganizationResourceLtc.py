import hashlib
import secrets
from fhir_data_generator import OrganizationLtc as Organization


class OrganizationResourceLtc:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.resource = resource
        self.organization_payload = item_dict['payload']

    def generate_organization_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        organization_class = Organization(resource_id)

        organization_class.set_profile_urls(self.organization_payload['profile_urls'])

        organization_class.set_identifiers(self.organization_payload['identifiers'])

        organization_class.set_active(self.organization_payload['active'])

        organization_class.set_type(self.organization_payload['types'])

        organization_class.set_name(self.organization_payload['name'])

        organization_class.set_telecom(self.organization_payload['telecom'])

        organization_class.set_address(self.organization_payload['address'])

        organization_class.set_contact(self.organization_payload['contact'])

        organization_class.create()

        return organization_class.payload_template
