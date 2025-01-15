from .goal import *
from .patient import *
from .care_plan import *
from .condition import *
from .practitioner import *

from fastapi import APIRouter


patient_router = APIRouter(tags=['Generate Patient Resource'], prefix='/api/v1')
patient_router.add_api_route('/track13_2024_patient', generate_track13_2024_for_patient, methods=['POST'], description='Generate Track13 2024 Patient Resource')

practitioner_router = APIRouter(tags=['Generate Practitioner Resource'], prefix='/api/v1')
practitioner_router.add_api_route('/track13_2024_practitioner', generate_track13_2024_for_practitioner, methods=['POST'], description='Generate Track13 2024 Practitioner Resource')

goal_router = APIRouter(tags=['Generate Goal Resource'], prefix='/api/v1')
goal_router.add_api_route('/track13_2024_goal', generate_track13_2024_for_goal, methods=['POST'], description='Generate Track13 2024 Goal Resource')

care_plan_router = APIRouter(tags=['Generate CarePlan Resource'], prefix='/api/v1')
care_plan_router.add_api_route('/track13_2024_care_plan', generate_track13_2024_for_care_plan, methods=['POST'], description='Generate Track13 2024 CarePlan Resource')

condition_router = APIRouter(tags=['Generate Condition Resource'], prefix='/api/v1')
condition_router.add_api_route('/track13_2024_condition', generate_track13_2024_for_condition, methods=['POST'], description='Generate Track13 2024 Condition Resource')
