import hashlib
import secrets
from fhir_data_generator import AdverseEventLtc as AdverseEvent


class AdverseEventResourceLtc:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.adverse_event_payload = item_dict['payload']
        self.type = item_dict['type']
        self.resource = resource

    def generate_adverse_event_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        adverse_event_class = AdverseEvent(resource_id)

        if self.type == 'cs100':
            adverse_event_class.set_profile_urls(self.adverse_event_payload['profile_urls'])

            adverse_event_class.set_extension(self.adverse_event_payload['extension'])

            adverse_event_class.set_identifier(self.adverse_event_payload['identifier'])

            adverse_event_class.set_actuality(self.adverse_event_payload['actuality'])

            adverse_event_class.set_event(self.adverse_event_payload['event'])

            adverse_event_class.set_subject(self.adverse_event_payload['subject'])

            adverse_event_class.set_date(self.adverse_event_payload['date'])

            adverse_event_class.set_recorded_date(self.adverse_event_payload['recorded_date'])

        if self.type == 'ltc':
            adverse_event_class.set_profile_urls(self.adverse_event_payload['profile_urls'])

            adverse_event_class.set_identifier(self.adverse_event_payload['identifier'])

            adverse_event_class.set_actuality(self.adverse_event_payload['actuality'])

            adverse_event_class.set_event(self.adverse_event_payload['event'])

            adverse_event_class.set_subject(self.adverse_event_payload['subject'])

            adverse_event_class.set_date(self.adverse_event_payload['date'])

            adverse_event_class.set_detected(self.adverse_event_payload['detected'])

            adverse_event_class.set_location(self.adverse_event_payload['location'])

            adverse_event_class.set_seriousness(self.adverse_event_payload['seriousness'])

            adverse_event_class.set_severity(self.adverse_event_payload['severity'])

            adverse_event_class.set_outcome(self.adverse_event_payload['outcome'])

            adverse_event_class.set_recorder(self.adverse_event_payload['recorder'])

            adverse_event_class.set_recorded_date(self.adverse_event_payload['recorded_date'])

        adverse_event_class.create()

        return adverse_event_class.payload_template
