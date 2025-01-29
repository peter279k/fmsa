import hashlib
import secrets
from fhir_data_generator import DocumentReferenceImri as DocumentReference


class Track8ForDocumentReference:
    def __init__(self, resource, item_dict: dict):
        self.item_dict = item_dict
        self.document_reference_payload = item_dict['payload']
        self.resource = resource

    def generate_document_reference_resource(self):
        resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        document_reference_class = DocumentReference(resource_id)

        document_reference_class.set_profile_urls(self.document_reference_payload['profile_urls'])

        document_reference_class.set_status(self.document_reference_payload['status'])

        document_reference_class.set_subject(self.document_reference_payload['subject'])

        document_reference_class.set_content(self.document_reference_payload['content'])

        document_reference_class.create()

        return document_reference_class.payload_template
