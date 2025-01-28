import hashlib
import secrets
from fhir_data_generator import TWCoreDiagnosticReport as DiagnosticReport


class Track8ForDiagnosticReport:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.resource = resource
        self.diagnostic_report_payload = item_dict['payload']

    def generate_diagnostic_report_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        diagnostic_report_class = DiagnosticReport(resource_id)

        profile_urls = self.diagnostic_report_payload['profile_urls']
        diagnostic_report_class.set_profile_urls(profile_urls)

        diagnostic_report_class.set_status(self.diagnostic_report_payload['status'])

        diagnostic_report_class.set_code_coding(self.diagnostic_report_payload['code_coding'])

        diagnostic_report_class.set_subject(self.diagnostic_report_payload['subject'])

        diagnostic_report_class.set_result(self.diagnostic_report_payload['result'])

        diagnostic_report_class.create()

        return diagnostic_report_class.payload_template
