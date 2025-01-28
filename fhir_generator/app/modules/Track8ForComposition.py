import hashlib
import secrets
from fhir_data_generator import TWCoreComposition as Composition


class Track8ForComposition:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.composition_payload = item_dict['payload']
        self.resource = resource

    def generate_composition_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        composition_class = Composition(resource_id)

        composition_class.set_profile_urls(self.composition_payload['profile_urls'])

        composition_class.set_identifier(self.composition_payload['identifier'])

        composition_class.set_status(self.composition_payload['status'])

        composition_class.set_type_coding(self.composition_payload['type_coding'])

        composition_class.set_subject(self.composition_payload['subject'])

        composition_class.set_date(self.composition_payload['date'])

        composition_class.set_author(self.composition_payload['author'])

        composition_class.set_title(self.composition_payload['title'])

        composition_class.set_section_title(self.composition_payload['section_title'])
        composition_class.set_section_code(self.composition_payload['section_code'])
        composition_class.set_section_entry(self.composition_payload['section_entry'])

        composition_class.create()

        return composition_class.payload_template
