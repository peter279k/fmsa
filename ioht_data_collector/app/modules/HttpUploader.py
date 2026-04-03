import httpx
from httpx import Response
from app.modules.interfaces.Connection import *


class HttpUploader(Connector, ResponseProcessor):
    def connect(self, info: dict):
        url = info['url']
        request_body = info['body']
        request_header = info['header']
        httpx.post(url, json=request_body, headers=request_header)

        print('Using httpx to connect and send request.')

    def process(self, response: Response):
        return {
            'status': response.status_code,
            'message': '',
            'data': response.json(),
        }
