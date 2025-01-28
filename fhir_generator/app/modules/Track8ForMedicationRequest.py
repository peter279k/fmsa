import hashlib
import secrets
from fhir_data_generator import TWCoreMedicationRequest as MedicationRequest


class Track8ForMedicationRequest:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.medication_request_payload = item_dict['payload']
        self.resource = resource

    def generate_medication_request_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        medication_request_class = MedicationRequest(resource_id)

        medication_request_class.set_profile_urls(self.medication_request_payload['profile_urls'])
        medication_request_class.set_status(self.medication_request_payload['status'])

        medication_request_class.set_intent(self.medication_request_payload['intent'])

        medication_request_class.set_medication_codeable_concept(self.medication_request_payload['medication_codeable_concept'])

        medication_request_class.set_subject(self.medication_request_payload['subject'])

        medication_request_class.set_encounter(self.medication_request_payload['encounter'])

        medication_request_class.set_requester(self.medication_request_payload['requester'])

        medication_request_class.set_performer(self.medication_request_payload['performer'])

        medication_request_class.set_based_on(self.medication_request_payload['based_on'])

        medication_request_class.create()

        return medication_request_class.payload_template
