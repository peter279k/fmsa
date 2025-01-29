import hashlib
import secrets
from fhir_data_generator import EncounterImri
from fhir_data_generator import TWCoreEncounter as Encounter


class Track8ForEncounter:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.resource = resource
        self.encounter_payload = item_dict['payload']

    def generate_encounter_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        encounter_class = Encounter(resource_id)

        profile_urls = self.encounter_payload['profile_urls']
        encounter_class.set_profile_urls(profile_urls)

        encounter_class.set_extension(self.encounter_payload['extension'])

        encounter_class.set_identifier(self.encounter_payload['identifiers'])

        encounter_class.set_status(self.encounter_payload['status'])

        encounter_class.set_class(self.encounter_payload['fixture_class'])

        encounter_class.set_service_type_coding(self.encounter_payload['service_type_coding'])

        encounter_class.set_subject(self.encounter_payload['subject'])

        encounter_class.set_participant_individual(self.encounter_payload['participant_individual'])

        encounter_class.set_period(self.encounter_payload['period'])

        encounter_class.set_length(self.encounter_payload['length'])

        encounter_class.create()

        return encounter_class.payload_template

    def generate_encounter_min_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        encounter_class = EncounterImri(resource_id)

        profile_urls = self.encounter_payload['profile_urls']
        encounter_class.set_profile_urls(profile_urls)

        encounter_class.set_status(self.encounter_payload['status'])

        encounter_class.set_class(self.encounter_payload['fixture_class'])

        encounter_class.set_service_type_coding(self.encounter_payload['service_type_coding'])

        encounter_class.set_subject(self.encounter_payload['subject'])

        encounter_class.set_participant_individual(self.encounter_payload['participant_individual'])

        encounter_class.set_period(self.encounter_payload['period'])

        encounter_class.set_hospitalization(self.encounter_payload['hospitalization'])

        encounter_class.create()

        return encounter_class.payload_template
