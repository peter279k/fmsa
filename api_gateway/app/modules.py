import os
import json
import redis
import httpx
from urllib.parse import urlencode


class CacheAccessToken:
    def __init__(self):
        self.host = 'api_gateway_access_token_storage'
        self.password = os.getenv('REDIS_PASSWORD')
        self.port = 6379
        self.db = 0

    def store_cache(self, username: str, user_login_response: dict):
        r = redis.Redis(host=self.host, port=self.port, password=self.password, db=self.db)
        result = r.set(username, json.dumps(user_login_response))

        return result

class KeyCloakAdmin:
    def __init__(self):
        self.x_form_urlencoded = 'application/x-www-form-urlencoded'
        self.keycloak_root = 'http://keycloak_adapter:8080'
        self.realm = 'fmsa'
        self.client_id = 'fmsa'
        self.client_uuid = ''
        self.auth_headers = {
            'Authorization': '',
        }

    def user_login(self, username: str, password: str):
        req_url = f'{self.keycloak_root}/realms/{self.realm}/protocol/openid-connect/token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
        }
        resp = httpx.post(
            req_url,
            headers=headers,
            data=urlencode({
                'client_id': self.client_id,
                'username': username,
                'password': password,
                'grant_type': 'password',
            })
        )

        return resp

    def admin_login(self):
        admin_username = os.getenv('KEYCLOAK_ADMIN')
        admin_password = os.getenv('KEYCLOAK_ADMIN_PASSWORD')
        req_url = f'{self.keycloak_root}/realms/master/protocol/openid-connect/token'
        headers = {
            'Content-Type': self.x_form_urlencoded,
        }
        post_data = {
            'username': admin_username,
            'password': admin_password,
            'grant_type': 'password',
            'client_id': 'admin-cli',
        }

        return httpx.post(req_url, data=post_data, headers=headers)

    def create_client_id(self, access_token: str):
        self.auth_headers['Authorization'] = f'Bearer {access_token}'
        client_settings = {
            'protocol': 'openid-connect',
            'clientId': self.client_id,
            'enabled': True,
            'publicClient': True,
            'standardFlowEnabled': True,
            'serviceAccountsEnabled': False,
            'directAccessGrantsEnabled': True,
            'attributes': {
                'oauth2.device.authorization.grant.enabled': True,
            },
        }

        response = httpx.post(
            f'{self.keycloak_root}/admin/realms/{self.realm}/clients',
            json=client_settings,
            headers=self.auth_headers,
        )

        return response

    def check_client_id_is_existed(self, access_token: str):
        self.auth_headers['Authorization'] = f'Bearer {access_token}'
        response = httpx.get(
            f'{self.keycloak_root}/admin/realms/{self.realm}/clients',
            headers=self.auth_headers,
        )

        is_existed = False
        for record in response.json():
            if record['clientId'] == self.client_id:
                self.client_uuid = record['id']
                is_existed = True
                break

        return is_existed

    def create_realm(self, access_token: str):
        self.auth_headers['Authorization'] = f'Bearer {access_token}'
        response = httpx.post(
            f'{self.keycloak_root}/admin/realms',
            headers=self.auth_headers,
            json={
                'realm': self.realm,
                'enabled': True,
            }
        )

        return response

    def check_realm_is_existed(self, access_token: str):
        self.auth_headers['Authorization'] = f'Bearer {access_token}'
        resp = httpx.get(
            f'{self.keycloak_root}/admin/realms',
            headers=self.auth_headers,
        )

        is_existed = False
        for record in resp.json():
            if record['realm'] == self.realm:
                is_existed = True
                break

        return is_existed

    def create_user(self, username: str, password: str, first_name: str, last_name: str, email: str):
        user_settings = {
            'username': username,
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
            'enabled': True,
            'credentials': [{
                'type': 'password',
                'value': password,
                'temporary': False,
            }]
        }
        resp = httpx.post(
            f'{self.keycloak_root}/admin/realms/{self.realm}/users',
            json=user_settings,
            headers=self.auth_headers,
        )

        return resp
