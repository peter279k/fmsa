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
from starlette.responses import Response, JSONResponse

from fastapi_gateway import route
from .depends import check_api_key
from .models import RegisterAccount
from .models import LoginAccount
from .modules import KeyCloakAdmin, CacheAccessToken


app = FastAPI(title='FMSA API Gateway')
account_router = APIRouter(prefix='/api/v1')
fhir_ig_manager_router = APIRouter(prefix='/api/v1')
fhir_profile_manager_router = APIRouter(prefix='/api/v1')
fhir_generator_router = APIRouter(prefix='/api/v1')
fhir_data_manager_router = APIRouter(prefix='/api/v1')


SERVICE_URLS = [
    'http://api_gateway:8000',
    'http://data_analysis_service:8000',
    'http://fhir_generator:8000',
    'http://ioht_data_collector:8000',
    'http://fhir_converter:8000',
    'http://fhir_ig_manager:8000',
    'http://fhir_profile_manager:8000',
    'http://fhir_data_manager:8000',
    'http://terminology_manager:8000',
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
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track13_2024_patient',
    service_path='/api/v1/track13_2024_patient',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track13 2024 Patient with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track13_2024_patient(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track13_2024_practitioner',
    service_path='/api/v1/track13_2024_practitioner',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track13 2024 Practitioner with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track13_2024_practitioner(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track13_2024_goal',
    service_path='/api/v1/track13_2024_goal',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track13 2024 Goal with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track13_2024_goal(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track13_2024_care_plan',
    service_path='/api/v1/track13_2024_care_plan',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track13 2024 CarePlan with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track13_2024_care_plan(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track13_2024_condition',
    service_path='/api/v1/track13_2024_condition',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track13 2024 Condition with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track13_2024_condition(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track13_2024_service_request',
    service_path='/api/v1/track13_2024_service_request',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track13 2024 ServiceRequest with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track13_2024_service_request(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track13_2024_observation',
    service_path='/api/v1/track13_2024_observation',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track13 2024 Observation with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track13_2024_observation(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_practitioner_role',
    service_path='/api/v1/track8_2024_practitioner_role',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 PractitionerRole Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_practitioner_role_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_practitioner',
    service_path='/api/v1/track8_2024_practitioner',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 Practitioner Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_practitioner_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_patient',
    service_path='/api/v1/track8_2024_patient',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track13 2024 Patient Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_patient_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_organization',
    service_path='/api/v1/track8_2024_organization',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 Organization Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_organization_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_observation',
    service_path='/api/v1/track8_2024_observation',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 Observation Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_observation_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_encounter',
    service_path='/api/v1/track8_2024_encounter',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 Encounter Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_encounter_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_diagnostic_report',
    service_path='/api/v1/track8_2024_diagnostic_report',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 DiagnosticReport Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_diagnostic_report_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_coverage',
    service_path='/api/v1/track8_2024_coverage',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 Coverage Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_coverage_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_condition',
    service_path='/api/v1/track8_2024_condition',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 Condition Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_condition_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_composition',
    service_path='/api/v1/track8_2024_composition',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 Composition Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_composition_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_claim',
    service_path='/api/v1/track8_2024_claim',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 Claim Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_claim_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_procedure',
    service_path='/api/v1/track8_2024_procedure',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 Procedure Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_procedure_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_medication_request',
    service_path='/api/v1/track8_2024_medication_request',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 MedicationRequest Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_medication_request_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_location',
    service_path='/api/v1/track8_2024_location',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 Location Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_location_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_imaging_study',
    service_path='/api/v1/track8_2024_imaging_study',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 ImagingStudy Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_imaging_study_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_document_reference',
    service_path='/api/v1/track8_2024_document_reference',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 DocumentReference Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_document_reference_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_generator_router.post,
    service_url=SERVICE_URLS[2],
    gateway_path='/track8_2024_care_plan',
    service_path='/api/v1/track8_2024_care_plan',
    status_code=status.HTTP_200_OK,
    tags=['Generate Track8 2024 CarePlan Resources with the fhir_generator'],
    dependencies=[Depends(check_api_key)],
)
async def track8_2024_care_plan_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_ig_manager_router.get,
    service_url=SERVICE_URLS[5],
    gateway_path='/ig',
    service_path='/api/v1/ig',
    status_code=status.HTTP_200_OK,
    tags=['Retrieve IG metadata with the fhir_ig_manager'],
    dependencies=[Depends(check_api_key)],
)
async def retrieve_ig(request: Request, response: Response):
    pass

@route(
    request_method=fhir_ig_manager_router.post,
    service_url=SERVICE_URLS[5],
    gateway_path='/create_ig_metadata',
    service_path='/api/v1/create_ig_metadata',
    status_code=status.HTTP_200_OK,
    tags=['Create IG metadata with the fhir_ig_manager'],
    dependencies=[Depends(check_api_key)],
)
async def create_ig_metadata(request: Request, response: Response):
    pass

@route(
    request_method=fhir_ig_manager_router.post,
    service_url=SERVICE_URLS[5],
    gateway_path='/upload_ig',
    service_path='/api/v1/upload_ig',
    status_code=status.HTTP_200_OK,
    tags=['Upload Archived IG file with the fhir_ig_manager'],
    dependencies=[Depends(check_api_key)],
)
async def upload_ig_file(request: Request, response: Response, file: UploadFile = File(...)):
    pass

@route(
    request_method=fhir_ig_manager_router.put,
    service_url=SERVICE_URLS[5],
    gateway_path='/update_ig_metadata',
    service_path='/api/v1/update_ig_metadata',
    status_code=status.HTTP_200_OK,
    tags=['Update IG metadata with the fhir_ig_manager'],
    dependencies=[Depends(check_api_key)],
)
async def update_ig_metadata(request: Request, response: Response):
    pass

@route(
    request_method=fhir_ig_manager_router.delete,
    service_url=SERVICE_URLS[5],
    gateway_path='/delete_ig_metadata',
    service_path='/api/v1/delete_ig_metadata',
    status_code=status.HTTP_200_OK,
    tags=['Delete IG metadata with the fhir_ig_manager'],
    dependencies=[Depends(check_api_key)],
)
async def delete_ig_metadata(request: Request, response: Response):
    pass

@route(
    request_method=fhir_profile_manager_router.get,
    service_url=SERVICE_URLS[6],
    gateway_path='/profile',
    service_path='/api/v1/profile',
    status_code=status.HTTP_200_OK,
    tags=['Retrieve Profile metadata with the fhir_profile_manager'],
    dependencies=[Depends(check_api_key)],
)
async def profile(request: Request, response: Response):
    pass

@route(
    request_method=fhir_profile_manager_router.post,
    service_url=SERVICE_URLS[6],
    gateway_path='/create_profile_metadata',
    service_path='/api/v1/create_profile_metadata',
    status_code=status.HTTP_200_OK,
    tags=['Create Profile metadata with the fhir_profile_manager'],
    dependencies=[Depends(check_api_key)],
)
async def create_profile_metadata(request: Request, response: Response):
    pass

@route(
    request_method=fhir_profile_manager_router.put,
    service_url=SERVICE_URLS[6],
    gateway_path='/update_profile_metadata',
    service_path='/api/v1/update_profile_metadata',
    status_code=status.HTTP_200_OK,
    tags=['Update Profile metadata with the fhir_profile_manager'],
    dependencies=[Depends(check_api_key)],
)
async def update_profile_metadata(request: Request, response: Response):
    pass

@route(
    request_method=fhir_profile_manager_router.delete,
    service_url=SERVICE_URLS[6],
    gateway_path='/delete_profile_metadata',
    service_path='/api/v1/delete_profile_metadata',
    status_code=status.HTTP_200_OK,
    tags=['Delete Profile metadata with the fhir_profile_manager'],
    dependencies=[Depends(check_api_key)],
)
async def delete_profile_metadata(request: Request, response: Response):
    pass

@route(
    request_method=fhir_profile_manager_router.post,
    service_url=SERVICE_URLS[6],
    gateway_path='/upload_profile',
    service_path='/api/v1/upload_profile',
    status_code=status.HTTP_200_OK,
    tags=['Upload Profile to FHIR Server Adapter with the fhir_profile_manager'],
    dependencies=[Depends(check_api_key)],
)
async def upload_profile(request: Request, response: Response):
    pass

@route(
    request_method=fhir_profile_manager_router.get,
    service_url=SERVICE_URLS[6],
    gateway_path='/retrieve_profile',
    service_path='/api/v1/retrieve_profile',
    status_code=status.HTTP_200_OK,
    tags=['Retrieve Profile to FHIR Server Adapter with the fhir_profile_manager'],
    dependencies=[Depends(check_api_key)],
)
async def retrieve_profile(request: Request, response: Response):
    pass

@route(
    request_method=fhir_data_manager_router.post,
    service_url=SERVICE_URLS[7],
    gateway_path='/upload/{resource_name}',
    service_path='/api/v1/upload/{resource_name}',
    status_code=status.HTTP_200_OK,
    tags=['Upload FHIR resource with the fhir_data_manager'],
    dependencies=[Depends(check_api_key)],
)
async def upload_resource(request: Request, response: Response):
    pass

@route(
    request_method=fhir_data_manager_router.get,
    service_url=SERVICE_URLS[7],
    gateway_path='/retrieve/{resource_name}',
    service_path='/api/v1/retrieve/{resource_name}',
    status_code=status.HTTP_200_OK,
    tags=['Retrieve FHIR resource with the fhir_data_manager'],
    dependencies=[Depends(check_api_key)],
)
async def retrieve_track13_2024_service_request(request: Request, response: Response):
    pass


app.include_router(account_router)
app.include_router(fhir_ig_manager_router)
app.include_router(fhir_profile_manager_router)
app.include_router(fhir_generator_router)
app.include_router(fhir_data_manager_router)
