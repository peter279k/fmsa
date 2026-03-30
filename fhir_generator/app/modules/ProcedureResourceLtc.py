import hashlib
import secrets
from fhir_data_generator import ProcedureLtc as Procedure


class ProcedureResourceLtc:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.procedure_payload = item_dict['payload']
        self.resource = resource

    def generate_procedure_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        procedure_class = Procedure(resource_id)

        procedure_class.set_profile_urls(self.procedure_payload['profile_urls'])

        procedure_class.set_status(self.procedure_payload['status'])

        procedure_class.set_code_coding(self.procedure_payload['code_codings'])
        procedure_class.set_code_text(self.procedure_payload['code_texts'])

        procedure_class.set_subject(self.procedure_payload['subject'])

        procedure_class.set_performer(self.procedure_payload['performer'])

        procedure_class.set_performed_date_time(self.procedure_payload['performed_date_time'])

        procedure_class.set_note(self.procedure_payload['note'])

        procedure_class.create()

        return procedure_class.payload_template
