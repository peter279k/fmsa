from .analysis import *

from fastapi import APIRouter


analysis_router = APIRouter(tags=['Data Analysis'], prefix='/api/v1')
analysis_router.add_api_route('/analyze', do_analysis, methods=['POST'], description='Analyze numeric array with specific params')
