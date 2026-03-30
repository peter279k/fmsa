import hashlib
import secrets
from fhir_data_generator import MedicationAdministrationLtc as MedicationAdministration


class MedicationAdministrationLtc:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.medication_administration_payload = item_dict['payload']
        self.resource = resource

    def generate_medication_request_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        medication_administration_class = MedicationAdministration(resource_id)

        medication_administration_class.set_profile_urls(self.medication_administration_payload['profile_urls'])

        medication_administration_class.set_status(self.medication_administration_payload['status'])

        medication_administration_class.set_medication_codeable_concept_coding(self.medication_administration_payload['medication_codeable_concept_coding'])
        medication_administration_class.set_medication_codeable_concept_text(self.medication_administration_payload['medication_codeable_concept_text'])

        medication_administration_class.set_subject(self.medication_administration_payload['subject'])

        medication_administration_class.set_effective_date_time(self.medication_administration_payload['effective_date_time'])

        medication_administration_class.set_performer(self.medication_administration_payload['performer'])

        medication_administration_class.set_note(self.medication_administration_payload['note'])

        medication_administration_class.set_dosage(self.medication_administration_payload['dosage'])

        medication_administration_class.create()

        return medication_administration_class.payload_template
