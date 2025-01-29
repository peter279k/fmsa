import hashlib
import secrets
from fhir_data_generator import ConditionImri
from fhir_data_generator import TWCoreCondition as Condition


class Track8ForCondition:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.condition_payload = item_dict['payload']
        self.resource = resource

    def generate_condition_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        condition_class = Condition(resource_id)

        condition_class.set_profile_urls(self.condition_payload['profile_urls'])

        condition_class.set_identifier(self.condition_payload['identifier'])

        condition_class.set_clinical_status_coding(self.condition_payload['clinical_status_coding'])

        condition_class.set_category_coding(self.condition_payload['category_coding'])

        condition_class.set_code_coding(self.condition_payload['code_coding'])

        condition_class.set_subject(self.condition_payload['subject'])

        condition_class.set_encounter(self.condition_payload['encounter'])

        condition_class.set_recorded_date(self.condition_payload['recorded_date'])

        condition_class.set_recorder(self.condition_payload['recorder'])

        condition_class.set_asserter(self.condition_payload['asserter'])

        condition_class.set_stage(self.condition_payload['stage'])

        condition_class.set_note(self.condition_payload['note'])

        condition_class.create()

        return condition_class.payload_template

    def generate_condition_chief_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        condition_class = ConditionImri(resource_id)

        condition_class.set_profile_urls(self.condition_payload['profile_urls'])

        condition_class.set_clinical_status_coding(self.condition_payload['clinical_status_coding'])

        condition_class.set_category_coding(self.condition_payload['category_coding'])

        condition_class.set_code_coding(self.condition_payload['code_coding'])
        condition_class.set_code_text(self.condition_payload['code_text'])

        condition_class.set_subject(self.condition_payload['subject'])

        condition_class.set_encounter(self.condition_payload['encounter'])

        condition_class.set_note(self.condition_payload['note'])

        condition_class.create()

        return condition_class.payload_template
