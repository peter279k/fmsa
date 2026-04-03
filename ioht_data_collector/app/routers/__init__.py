from .collector_router import *

from fastapi import APIRouter


data_collector_router = APIRouter(tags=['Upload Observation Resource'], prefix='/api/v1')
data_collector_router.add_api_route('/observation_resource', upload_observation_resource_data, methods=['POST'], description='Upload Observation Resource')
