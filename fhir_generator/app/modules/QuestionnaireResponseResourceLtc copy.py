import hashlib
import secrets
from fhir_data_generator import QuestionnaireResponseLtc as QuestionnaireResponse


class QuestionnaireResponseResourceLtc:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.questionnaire_response_payload = item_dict['payload']
        self.resource = resource

    def generate_questionnaire_response_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        questionnaire_response_class = QuestionnaireResponse(resource_id)
        questionnaire_response_class.set_profile_urls(self.questionnaire_response_payload['profile_urls'])

        questionnaire_response_class.set_extension(self.questionnaire_response_payload['extensions'])

        questionnaire_response_class.set_questionnaire(self.questionnaire_response_payload['questionnaires'])

        questionnaire_response_class.set_status(self.questionnaire_response_payload['status'])

        questionnaire_response_class.set_subject(self.questionnaire_response_payload['subject'])

        questionnaire_response_class.set_authored(self.questionnaire_response_payload['authored_lists'])

        questionnaire_response_class.set_author(self.questionnaire_response_payload['author'])

        questionnaire_response_class.set_source(self.questionnaire_response_payload['source'])

        questionnaire_response_class.set_item(self.questionnaire_response_payload['items'])

        questionnaire_response_class.create()

        return questionnaire_response_class.payload_template
