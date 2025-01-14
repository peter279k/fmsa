from .care_plan import *
from fastapi import APIRouter


care_plan_router = APIRouter(tags=['Generate CarePlan Resource'], prefix='/api/v1')
care_plan_router.add_api_route('/generate_care_plan', generate_care_plan, methods=['GET'], description='Generate CarePlan Resource')
