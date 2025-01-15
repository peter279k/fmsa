import httpx


class RetrieveResource:
    def __init__(self, resource_name: str, query_params: str):
        self.headers = {
            'Accept': 'application/fhir+json',
        }
        self.fhir_server_url = f'http://fhir-server-adapter:8080/fhir/{resource_name}'

        if query_params != '':
            self.fhir_server_url = f'http://fhir-server-adapter:8080/fhir/{resource_name}?{query_params}'

    def retrieve(self):
        response = httpx.get(
            self.fhir_server_url,
            headers=self.headers
        )

        return response
