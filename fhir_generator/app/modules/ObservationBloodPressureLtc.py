import hashlib
import secrets
from fhir_data_generator import ObservationLtc as Observation


class ObservationBloodPressureLtc:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.observation_payload = item_dict['payload']
        self.resource = resource

    def generate_observation_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        observation_class = Observation(resource_id)

        profile_urls = self.observation_payload['profile_urls']
        observation_class.set_profile_urls(profile_urls)

        observation_class.set_status(self.observation_payload['status'])

        observation_class.set_category_coding(self.observation_payload['category_coding'])

        observation_class.set_code_coding(self.observation_payload['code_coding'])

        observation_class.set_subject(self.observation_payload['subject'])

        observation_class.set_effective_datetime(self.observation_payload['effective_datetime'])

        observation_class.set_performer(self.observation_payload['performer'])

        observation_class.set_interpretation(self.observation_payload['interpretation'])

        observation_class.set_note(self.observation_payload['note'])

        observation_class.set_body_site_coding(self.observation_payload['body_site_coding'])

        observation_class.set_method_coding(self.observation_payload['method_coding'])

        observation_class.set_component(self.observation_payload['component'])

        observation_class.create()

        return observation_class.payload_template
