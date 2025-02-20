from .converter import *

from fastapi import APIRouter


converter_router = APIRouter(tags=['FHIR Converter'], prefix='/api/v1')
converter_router.add_api_route('/convert', convert_to_fhir, methods=['POST'], description='Retrieve Terminology metadata via specific params')
