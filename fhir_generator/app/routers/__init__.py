from .patient import *
from .care_plan import *
from fastapi import APIRouter


#care_plan_router = APIRouter(tags=['Generate CarePlan Resource'], prefix='/api/v1')
#care_plan_router.add_api_route('/generate_care_plan', generate_care_plan, methods=['GET'], description='Generate CarePlan Resource')

patient_router = APIRouter(tags=['Generate Patient Resource'], prefix='/api/v1')
patient_router.add_api_route('/track13_2024_patient', generate_track13_2024_for_patient, methods=['POST'], description='Generate Track13 2024 Patient Resource')
