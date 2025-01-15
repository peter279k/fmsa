from .upload import *
from .retrieve import *

from fastapi import APIRouter


upload_resource_router = APIRouter(tags=['Upload Specific FHIR Resource'], prefix='/api/v1')
upload_resource_router.add_api_route('/upload/{resource_name}', upload_resource, methods=['POST'], description='Upload Specific FHIR Resource')

# retrieve_resource_router = APIRouter(tags=['Retrieve Specific FHIR Resource'], prefix='/api/v1')
# retrieve_resource_router.add_api_route('/retrieve/{resource_name}', retrieve_resource, methods=['GET'], description='Retrieve Specific FHIR Resource')
