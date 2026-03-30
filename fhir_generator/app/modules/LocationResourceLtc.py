import hashlib
import secrets
from fhir_data_generator import LocationLtc as Location


class LocationResourceLtc:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.location_payload = item_dict['payload']
        self.resource = resource

    def generate_location_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        location_class = Location(resource_id)

        location_class.set_profile_urls(self.location_payload['profile_urls'])

        location_class.set_status(self.location_payload['status'])

        location_class.set_name(self.location_payload['name'])

        location_class.set_description(self.location_payload['description'])

        location_class.set_mode(self.location_payload['mode'])

        location_class.set_type(self.location_payload['types'])

        location_class.set_address(self.location_payload['address'])

        location_class.set_position(self.location_payload['position'])

        location_class.create()

        return location_class.payload_template
