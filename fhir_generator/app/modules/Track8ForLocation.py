import hashlib
import secrets
from fhir_data_generator import LocationImri as Location


class Track8ForLocation:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.location_payload = item_dict['payload']
        self.resource = resource

    def generate_location_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        location_class = Location(resource_id)

        location_class.set_profile_urls(self.location_payload['profile_urls'])

        location_class.set_identifier(self.location_payload['identifier'])

        location_class.set_name(self.location_payload['name'])

        location_class.create()

        return location_class.payload_template
