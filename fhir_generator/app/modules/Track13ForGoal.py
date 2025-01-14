import hashlib
import secrets
from fhir_data_generator import Goal


class Track13ForGoal:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.goal_payload = item_dict['goal_payload']
        self.resource = resource

    def generate_goal_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        goal_class = Goal(resource_id)

        goal_class.set_profile_urls(self.goal_payload['profile_urls'])

        goal_class.set_identifiers(self.goal_payload['identifiers'])

        goal_class.set_lifecycle_status(self.goal_payload['lifecycle_status'])

        goal_class.set_category_coding(self.goal_payload['category_coding'])

        goal_class.set_description_text(self.goal_payload['description_text'])

        goal_class.set_subject(self.goal_payload['subject'])

        goal_class.set_target_measure_coding(self.goal_payload['target_measure_coding'])
        goal_class.set_target_detail_quantity(self.goal_payload['target_detail_quantity'])

        goal_class.create()

        return goal_class.payload_template
