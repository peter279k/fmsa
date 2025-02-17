from .upload import *
from .retrieve import *

from fastapi import APIRouter


upload_resource_router = APIRouter(tags=['Upload Specific FHIR Resource'], prefix='/api/v1')
upload_resource_router.add_api_route('/upload/{resource_name}', upload_resource, methods=['POST'], description='Upload Specific FHIR Resource')
upload_resource_router.add_api_route('/update/{resource_name}', update_resource, methods=['PUT'], description='Update Specific FHIR Resource')

delete_resource_router = APIRouter(tags=['Delete Specific FHIR Resource'], prefix='/api/v1')
delete_resource_router.add_api_route('/delete/{resource_name}/{resource_id}', delete_resource, methods=['DELETE'], description='Delete Specific FHIR Resource')

retrieve_resource_router = APIRouter(tags=['Retrieve Specific FHIR Resource'], prefix='/api/v1')
retrieve_resource_router.add_api_route('/retrieve/{resource_name}', retrieve_resource, methods=['GET'], description='Retrieve Specific FHIR Resource')

hapi_fhir_server_adapter_router = APIRouter(tags=['Interacting the HAPI FHIR server adapter'], prefix='/api/v1')
hapi_fhir_server_adapter_router.add_api_route('/import_archived_code_system', import_archived_code_system, methods=['GET'], description='Import specific archived code system file')
hapi_fhir_server_adapter_router.add_api_route('/retrieve_code_system_log', retrieve_code_system_log, methods=['GET'], description='Retrieve specific code system importing log')
