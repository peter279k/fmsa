import hashlib
import secrets
from fhir_data_generator import ConditionE as Condition


class Track13ForCondition:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.condition_payload = item_dict['condition_payload']
        self.resource = resource

    def generate_condition_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        condition_class = Condition(resource_id)

        condition_class.set_profile_urls(self.condition_payload['profile_urls'])

        condition_class.set_clinical_status_coding(self.condition_payload['clinical_status_coding'])

        condition_class.set_category_coding(self.condition_payload['category_coding'])

        condition_class.set_code_coding(self.condition_payload['code_coding'])

        if self.condition_payload.get('code_text') is not None:
            condition_class.set_code_text(self.condition_payload['code_text'])

        condition_class.set_subject(self.condition_payload['subject'])

        condition_class.set_asserter(self.condition_payload['asserter'])

        condition_class.create()

        return condition_class.payload_template
