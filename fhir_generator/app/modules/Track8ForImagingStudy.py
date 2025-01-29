import hashlib
import secrets
from fhir_data_generator import ImagingStudyImri as ImagingStudy


class Track8ForImagingStudy:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.imaging_study_payload = item_dict['payload']
        self.resource = resource

    def generate_imaging_study_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        imaging_study_class = ImagingStudy(resource_id)

        imaging_study_class.set_profile_urls(self.imaging_study_payload['profile_urls'])

        imaging_study_class.set_status(self.imaging_study_payload['status'])

        imaging_study_class.set_subject(self.imaging_study_payload['subject'])

        imaging_study_class.set_encounter(self.imaging_study_payload['encounter'])

        imaging_study_class.set_started(self.imaging_study_payload['started'])

        imaging_study_class.set_interpreter(self.imaging_study_payload['interpreter'])

        imaging_study_class.set_description(self.imaging_study_payload['description'])

        imaging_study_class.create()

        return imaging_study_class.payload_template
