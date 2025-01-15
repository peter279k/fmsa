import hashlib
import secrets
from fhir_data_generator import PhysicalActivityServiceRequest as ServiceRequest


class Track13ForServiceRequest:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.service_request_payload = item_dict['service_request_payload']
        self.resource = resource

    def generate_service_request_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        service_request_class = ServiceRequest(resource_id)

        profile_urls = self.service_request_payload['profile_urls']
        service_request_class.set_profile_urls(profile_urls)

        service_request_class.set_identifiers(self.service_request_payload['identifiers'])

        service_request_class.set_status(self.service_request_payload['status'])

        service_request_class.set_intent(self.service_request_payload['intent'])

        service_request_class.set_category_coding(self.service_request_payload['category_coding'])

        service_request_class.set_code_coding(self.service_request_payload['code_coding'])

        service_request_class.set_subject(self.service_request_payload['subject'])

        service_request_class.set_authored_on(self.service_request_payload['authored_on'])

        service_request_class.set_requester(self.service_request_payload['requester'])

        service_request_class.create()

        return service_request_class.payload_template
