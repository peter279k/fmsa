from .manager import *

from fastapi import APIRouter


manager_router = APIRouter(tags=['Terminology Manager'], prefix='/api/v1')
manager_router.add_api_route('/terminology', retrieve_terminology, methods=['GET'], description='Retrieve Terminology metadata via specific params')
manager_router.add_api_route('/create_terminology_metadata', create_terminology_metadata, methods=['POST'], description='Create Terminology metadata')
manager_router.add_api_route('/upload_terminology', upload_terminology, methods=['POST'], description='Upload Terminology archived zip file')
manager_router.add_api_route('/update_terminology_metadata', update_terminology_metadata, methods=['PUT'], description='Update Terminology metadata')
manager_router.add_api_route('/delete_terminology_metadata', delete_terminology_metadata, methods=['DELETE'], description='Delete Terminology metadata')
manager_router.add_api_route('/retrieve_archived_code_system', retrieve_archived_code_system, methods=['GET'], description='Retrieve CodeSystem zip file via filename')
manager_router.add_api_route('/call_importing_archived_code_system', call_importing_archived_code_system, methods=['GET'], description='Importing archived CodeSystem via zip filename to fhir_data_manager (fhir_server_adapter)')
manager_router.add_api_route('/call_retrieving_code_system_log', call_retrieving_code_system_log, methods=['GET'], description='Importing archived CodeSystem via zip filename to fhir_data_manager (fhir_server_adapter)')

manager_router.add_api_route('/create_code_system', create_code_system, methods=['PUT'], description='Create specific CodeSystem to the fhir_data_manager (fhir_server_adapter)')
manager_router.add_api_route('/delete_code_system/{resource_id}', delete_code_system, methods=['DELETE'], description='Delete specific CodeSystem to the fhir_data_manager (fhir_server_adapter)')
