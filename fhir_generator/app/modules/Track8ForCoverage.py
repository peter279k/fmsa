import hashlib
import secrets
from fhir_data_generator import CoverageC1 as Coverage


class Track8ForCoverage:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.resource = resource
        self.coverage_payload = item_dict['payload']

    def generate_coverage_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        coverage_class = Coverage(resource_id)

        profile_urls = self.coverage_payload['profile_urls']
        coverage_class.set_profile_urls(profile_urls)

        coverage_class.set_status(self.coverage_payload['status'])

        coverage_class.set_beneficiary(self.coverage_payload['beneficiary'])

        coverage_class.set_payor(self.coverage_payload['payor'])

        coverage_class.create()

        return coverage_class.payload_template
