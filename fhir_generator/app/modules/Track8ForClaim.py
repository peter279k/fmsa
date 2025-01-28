import hashlib
import secrets
from fhir_data_generator import Claim


class Track8ForClaim:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.claim_payload = item_dict['payload']
        self.resource = resource

    def generate_claim_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        claim_class = Claim(resource_id)

        claim_class.set_profile_urls(self.claim_payload['profile_urls'])

        claim_class.set_identifier(self.claim_payload['identifier'])

        claim_class.set_status(self.claim_payload['status'])

        claim_class.set_type_coding(self.claim_payload['type_coding'])

        claim_class.set_patient(self.claim_payload['patient'])

        claim_class.set_created(self.claim_payload['created'])

        claim_class.set_provider(self.claim_payload['provider'])

        claim_class.set_priority_coding(self.claim_payload['priority_coding'])

        claim_class.set_diagnosis(self.claim_payload['diagnosis'])

        claim_class.set_insurance(self.claim_payload['insurance'])

        claim_class.set_item(self.claim_payload['item'])

        claim_class.set_total(self.claim_payload['total'])

        claim_class.create()

        return claim_class.payload_template
