import hashlib
import secrets
from fhir_data_generator import TWCoreProcedure as Procedure


class Track8ForProcedure:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.procedure_payload = item_dict['payload']
        self.resource = resource

    def generate_procedure_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        procedure_class = Procedure(resource_id)

        procedure_class.set_profile_urls(self.procedure_payload['profile_urls'])

        procedure_class.set_status(self.procedure_payload['status'])

        procedure_class.set_category(self.procedure_payload['category'])

        procedure_class.set_code_coding(self.procedure_payload['code_coding'])
        procedure_class.set_code_text(self.procedure_payload['code_text'])

        procedure_class.set_subject(self.procedure_payload['subject'])

        procedure_class.set_encounter(self.procedure_payload['encounter'])

        procedure_class.set_performed_date_time(self.procedure_payload['performed_date_time'])

        procedure_class.create()

        return procedure_class.payload_template
