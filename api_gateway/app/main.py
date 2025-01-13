import json
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import File
from fastapi import Form
from fastapi import UploadFile
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from fastapi_gateway import route
from .depends import check_api_key
from .models import RegisterAccount
from .models import LoginAccount
from .modules import KeyCloakAdmin, CacheAccessToken

from app.routers.api_gateway_router import api_gateway_router

app = FastAPI(title='FMSA API Gateway')
account_router = APIRouter(prefix='/api/v1')
fhir_generator_router = APIRouter(prefix='/api/v1/fhir_generator')

SERVICE_URLS = [
    'http://api_gateway:8000/api/v1',
    'http://data_analysis_service:8000/api/v1/data_analysis',
    'http://ioht_data_collector:8000/api/v1/ioht_data_collector',
    'http://fhir_generator:8000/api/v1/fhir_generator',
    'http://fhir_converter:8000/api/v1/fhir_converter',
    'http://fhir_ig_manager:8000/api/v1/fhir_ig_manager',
    'http://fhir_profile_manager:8000/api/v1/fhir_profile_manager',
    'http://fhir_data_manager:8000/api/v1/fhir_data_manager',
    'http://terminology_manager:8000/api/v1/terminology_manager',
]

auth_depend = OAuth2PasswordBearer(tokenUrl='/api/login', scheme_name='JWT')


@account_router.get('/', tags=['Retrieving the FMSA version'])
async def get_fmsa_version():
    return {
        'status': status.HTTP_200_OK,
        'data': [],
        'message': 'v1',
    }

@account_router.get('/initial', tags=['FMSA Wizard'])
async def initial_configuration(request: Request):
    keycloak_admin = KeyCloakAdmin()
    admin_login_response = keycloak_admin.admin_login()
    if admin_login_response.status_code != status.HTTP_200_OK:
        return {
            'status': admin_login_response.status_code,
            'data': [admin_login_response.json()],
            'message': 'Login KeyCloak admin account is failed.',
        }

    admin_login_response_json = admin_login_response.json()
    admin_access_token = admin_login_response_json['access_token']


    if keycloak_admin.check_realm_is_existed(admin_access_token) is False:
        keycloak_admin.create_realm(admin_access_token)

    client_id = ''
    if keycloak_admin.check_client_id_is_existed(admin_access_token) is False:
        create_client_id_response = keycloak_admin.create_client_id(admin_access_token)
        client_id = create_client_id_response.headers['Location'].split('/')[-1]

    return {
        'status': 200,
        'data': [{'client_id': client_id}],
        'message': 'FMSA configuration is sucessful.',
    }

@account_router.post('/login', tags=['FMSA acount managemnt'], description='Login the account')
async def login_account(request: Request, payload: LoginAccount):
    dict_payload = payload.model_dump()
    username = dict_payload['username']
    password = dict_payload['password']

    keycloak_admin = KeyCloakAdmin()
    user_login_response = keycloak_admin.user_login(username, password)

    if user_login_response.status_code != status.HTTP_200_OK:
        return {
            'status': user_login_response.status_code,
            'data': [user_login_response.json()],
            'message': 'Login KeyCloak account is failed.',
        }

    cache_access_token = CacheAccessToken()
    store_cached_result = cache_access_token.store_cache(username, user_login_response.json())

    if store_cached_result is not True:
        return {
            'status': 500,
            'data': [],
            'message': f'Caching {username} credential is failed.',
        }

    return {
        'status': user_login_response.status_code,
        'data': [user_login_response.json()],
        'message': 'Login KeyCloak account is successful.',
    }

@account_router.post('/register', tags=['FMSA acount managemnt'], description='Register the account')
async def register_account(request: Request, payload: RegisterAccount):
    dict_payload = payload.model_dump()
    username = dict_payload['username']
    password = dict_payload['password']
    first_name = dict_payload['first_name']
    last_name = dict_payload['last_name']
    email = dict_payload['email']

    keycloak_admin = KeyCloakAdmin()
    admin_login_response = keycloak_admin.admin_login()
    if admin_login_response.status_code != status.HTTP_200_OK:
        return {
            'status': admin_login_response.status_code,
            'data': [admin_login_response.json()],
            'message': 'Login KeyCloak admin account is failed.',
        }

    admin_login_response_json = admin_login_response.json()
    admin_access_token = admin_login_response_json['access_token']


    create_user_response = keycloak_admin.create_user(admin_access_token, username, password, first_name, last_name, email)
    try:
        create_user_response_json = create_user_response.json()
    except json.JSONDecodeError:
        create_user_response_json = {}

    return {
        'status': create_user_response.status_code,
        'data': [create_user_response_json],
        'message': '',
    }

@route(
    request_method=fhir_generator_router.get,
    service_url=SERVICE_URLS[3],
    gateway_path='/check_required_header',
    service_path='/api/v1/fhir_generator/generate_care_plan',
    status_code=status.HTTP_200_OK,
    tags=['Check_api_key dependency for fhir_generator'],
)
async def check_required_header(request: Request):
    check_api_key(request)
    pass


app.include_router(api_gateway_router)
app.include_router(account_router)
app.include_router(fhir_generator_router)
