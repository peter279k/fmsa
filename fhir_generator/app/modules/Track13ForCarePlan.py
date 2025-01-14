import hashlib
import secrets
from fhir_data_generator import CarePlan


class Track13ForCarePlan:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.care_plan_payload = item_dict['care_plan_payload']
        self.resource = resource

    def generate_care_plan_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        care_plan_class = CarePlan(resource_id)

        profile_urls = self.care_plan_payload['profile_urls']
        care_plan_class.set_profile_urls(profile_urls)

        care_plan_class.set_status(self.care_plan_payload['status'])

        care_plan_class.set_intent(self.care_plan_payload['intent'])

        care_plan_class.set_category_coding(self.care_plan_payload['category_coding'])

        care_plan_class.set_description(self.care_plan_payload['description'])

        care_plan_class.set_subject(self.care_plan_payload['subject'])

        care_plan_class.set_author(self.care_plan_payload['author'])

        care_plan_class.set_goal(self.care_plan_payload['goal'])

        care_plan_class.set_activity_progress(self.care_plan_payload['activity_progress'])
        care_plan_class.set_activity_detail(self.care_plan_payload['activity_detail'])

        care_plan_class.set_note(self.care_plan_payload['note'])

        care_plan_class.create()

        return care_plan_class.payload_template
