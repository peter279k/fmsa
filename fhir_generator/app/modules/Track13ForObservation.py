import hashlib
import secrets
from fhir_data_generator import PhysicalActivityObservation as Observation


class Track13ForObservation:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.observation_payload = item_dict['observation_payload']
        self.component_form = [
            'gaitcycle-r',
            'gaitcycle-l',
            'weighttraining',
            'gaittype-l',
            'gaittype-r',
            'treadmill',
            'bloodpressure',
        ]
        self.concept_form = ['gaittype-l', 'gaittype-r', 'weighttraining']
        self.has_member_form = 'tbw'
        self.body_site_form = ['gaitcycle-r', 'gaitcycle-l', 'gaittype-l', 'gaittype-r']
        self.resource = resource

    def generate_observation_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        observation_class = Observation(resource_id)

        profile_urls = self.observation_payload['profile_urls']
        observation_class.set_profile_urls(profile_urls)

        observation_class.set_status(self.observation_payload['status'])

        observation_class.set_category_coding(self.observation_payload['category_coding'])

        observation_class.set_code_coding(self.observation_payload['code_coding'])
        observation_class.set_code_text(self.observation_payload['code_text'])

        observation_class.set_subject(self.observation_payload['subject'])

        observation_class.set_effective_datetime(self.observation_payload['effective_datetime'])

        observation_class.set_performer(self.observation_payload['performer'])

        if self.observation_payload['type'] in self.component_form:
            observation_class.set_component(self.observation_payload['component'])
        else:
            observation_class.set_value_quantity(self.observation_payload['value_quantity'])

        if self.observation_payload['type'] in self.concept_form:
            observation_class.set_value_codeable_concept(self.observation_payload['value_codeable_concept'])
        if self.observation_payload['type'] == self.has_member_form:
            observation_class.set_has_member(self.observation_payload['has_member'])
        if self.observation_payload['type'] in self.body_site_form:
            observation_class.set_body_site(self.observation_payload['body_site'])

        observation_class.create()

        return observation_class.payload_template
