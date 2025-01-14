import hashlib
import secrets
from fhir_data_generator import PatientTW


class Track13ForPatient:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.patient_payload = item_dict['patient_payload']
        self.resource = resource

    def generate_patient_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        patient_class = PatientTW(resource_id)

        profile_urls = self.patient_payload['profile_urls']

        patient_class.set_profile_urls(profile_urls)

        patient_class.set_extension_url(self.patient_payload['extension_url'])
        patient_class.set_extension_value_age(self.patient_payload['extension_value_age'])
        patient_class.set_extension_extension_coding(self.patient_payload['extension_extension_coding'])
        patient_class.set_extension_extension_url(self.patient_payload['extension_extension_url'])

        patient_class.set_identifiers(self.patient_payload['identifiers'])

        patient_class.set_active(self.patient_payload['active'])

        patient_class.set_name_use(self.patient_payload['name_use'])
        patient_class.set_name_text(self.patient_payload['name_text'])

        patient_class.set_gender(self.patient_payload['gender'])

        patient_class.set_birth_date(self.patient_payload['birth_date'])

        patient_class.create()

        return patient_class.payload_template
