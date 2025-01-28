import hashlib
import secrets
from fhir_data_generator import PatientIclaimC1 as Patient


class Track8ForPatient:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.patient_payload = item_dict['payload']
        self.resource = resource

    def generate_patient_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        patient_class = Patient(resource_id)

        profile_urls = self.patient_payload['profile_urls']

        patient_class.set_profile_urls(profile_urls)

        patient_class.set_extension(self.patient_payload['extension'])

        patient_class.set_identifiers(self.patient_payload['identifiers'])

        patient_class.set_name_use(self.patient_payload['name_use'])
        patient_class.set_name_text(self.patient_payload['name_text'])

        patient_class.set_gender(self.patient_payload['gender'])

        patient_class.set_birth_date(self.patient_payload['birth_date'])

        patient_class.set_address(self.patient_payload['address'])

        patient_class.create()

        return patient_class.payload_template

    def generate_patient_imri_min_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        patient_class = Patient(resource_id)

        profile_urls = self.patient_payload['profile_urls']

        patient_class.set_profile_urls(profile_urls)

        patient_class.set_identifiers(self.patient_payload['identifiers'])

        patient_class.set_name_use(self.patient_payload['name_use'])
        patient_class.set_name_text(self.patient_payload['name_text'])

        patient_class.set_gender(self.patient_payload['gender'])

        patient_class.set_birth_date(self.patient_payload['birth_date'])

        patient_class.create()

        return patient_class.payload_template
