import httpx


class UploadResource:
    def __init__(self, resource_name: str, item_dict: dict):
        self.item_dict = item_dict
        self.headers = {
            'Accept': 'application/fhir+json',
            'Content-Type': 'application/fhir+json',
        }
        self.fhir_server_url = f'http://fhir-server-adapter:8080/fhir/{resource_name}'

    def upload(self):
        resource = self.item_dict['resource']
        response = httpx.post(
            self.fhir_server_url,
            headers=self.headers,
            json=resource
        )

        return response
