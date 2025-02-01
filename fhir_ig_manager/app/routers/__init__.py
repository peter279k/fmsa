from .manager import *

from fastapi import APIRouter


manager_router = APIRouter(tags=['Implementation Guide Manager'], prefix='/api/v1')
manager_router.add_api_route('/ig', retrieve_ig, methods=['GET'], description='Retrieve IG metadata via specific params')
