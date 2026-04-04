import httpx


class DirectedUploader:
    def __init__(self, resource_name, item_dict: dict):
        self.item_dict = item_dict
        self.payload = item_dict['payload']
        self.resource_name = resource_name

    def upload_resource(self):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        url = f'http://fhir_data_manager:8000/api/v1/update/{self.resource_name}'
        payload = {
            'resource': self.payload,
        }

        response = httpx.put(url, headers=headers, json=payload)

        return response
