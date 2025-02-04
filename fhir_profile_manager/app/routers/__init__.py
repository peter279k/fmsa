from .manager import *

from fastapi import APIRouter


manager_router = APIRouter(tags=['Profile StructureDefinition Manager'], prefix='/api/v1')
manager_router.add_api_route('/profile', retrieve_profile, methods=['GET'], description='Retrieve Profile via specific params')
manager_router.add_api_route('/create_profile_metadata', create_profile_metadata, methods=['POST'], description='Create Profile')
manager_router.add_api_route('/update_profile_metadata', update_profile_metadata, methods=['PUT'], description='Update Profile metadata')
manager_router.add_api_route('/delete_profile_metadata', delete_profile_metadata, methods=['DELETE'], description='Delete Profile metadata')

manager_router.add_api_route('/upload_profile', upload_profile, methods=['POST'], description='Upload specific Profile StructureDefinition')
