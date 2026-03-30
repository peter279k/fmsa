import hashlib
import secrets
from fhir_data_generator import PatientLtc as Patient


class PatientResourceLtc:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.patient_payload = item_dict['payload']
        self.type = item_dict['type']
        self.resource = resource

    def generate_patient_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        patient_class = Patient(resource_id)

        if self.type == 'ltc':
            patient_class.set_profile_urls(self.patient_payload['profile_urls'])

            patient_class.set_active(self.patient_payload['active'])

            patient_class.set_names(self.patient_payload['names'])

            patient_class.set_identifiers(self.patient_payload['identifiers'])

            patient_class.set_telecom(self.patient_payload['telecom'])

            patient_class.set_gender(self.patient_payload['gender'])

            patient_class.set_birth_date(self.patient_payload['birth_date'])

            patient_class.set_address(self.patient_payload['address'])

            patient_class.set_contact(self.patient_payload['contact'])

            patient_class.set_managing_organization(self.patient_payload['managing_organization'])

        if self.type == 'cs100':
            patient_class.set_names(self.patient_payload['names'])

            patient_class.set_identifiers(self.patient_payload['identifiers'])

        patient_class.create()

        return patient_class.payload_template
