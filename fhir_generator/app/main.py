from app.routers import *

from fastapi import FastAPI
from circuit_breaker import CircuitBreakerMiddleware, CircuitBreakerInputDto



description = '''
FHIR Generator is used to create the specific FHIR resources
'''
app = FastAPI(
    title='FHIR Generator',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    }
)

# app.add_middleware(
#     CircuitBreakerMiddleware,
#     circuit_breaker_input=CircuitBreakerInputDto(
#         exception_list=(Exception,),
#         half_open_retry_count=5,
#         half_open_retry_timeout_seconds=60,
#     ),
# )

app.include_router(claim_router)
app.include_router(location_router)
app.include_router(adverse_event_router)
app.include_router(document_reference_router)
app.include_router(imaging_study_router)
app.include_router(procedure_router)
app.include_router(medication_request_router)
app.include_router(medication_administration_router)
app.include_router(composition_router)
app.include_router(coverage_router)
app.include_router(care_plan_router)
app.include_router(patient_router)
app.include_router(organization_router)
app.include_router(practitioner_router)
app.include_router(practitioner_role_router)
app.include_router(questionnaire_response_router)
app.include_router(goal_router)
app.include_router(condition_router)
app.include_router(service_request_router)
app.include_router(observation_router)
app.include_router(encounter_router)
app.include_router(diagnostic_report_router)
