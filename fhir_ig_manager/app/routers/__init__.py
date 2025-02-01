from .manager import *

from fastapi import APIRouter


manager_router = APIRouter(tags=['Implementation Guide Manager'], prefix='/api/v1')
manager_router.add_api_route('/ig', retrieve_ig, methods=['GET'], description='Retrieve IG metadata via specific params')
manager_router.add_api_route('/create_ig_metadata', create_ig_metadata, methods=['POST'], description='Create IG metadata')
manager_router.add_api_route('/upload_ig', upload_ig, methods=['POST'], description='Upload IG archived zip file')
manager_router.add_api_route('/update_ig_metadata', update_ig_metadata, methods=['PUT'], description='Update IG metadata')
manager_router.add_api_route('/delete_ig_metadata', delete_ig_metadata, methods=['DELETE'], description='Delete IG metadata')
