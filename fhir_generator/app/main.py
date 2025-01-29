from app.routers import *

from fastapi import FastAPI


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

app.include_router(claim_router)
app.include_router(location_router)
app.include_router(document_reference_router)
app.include_router(imaging_study_router)
app.include_router(procedure_router)
app.include_router(medication_request_router)
app.include_router(composition_router)
app.include_router(coverage_router)
app.include_router(care_plan_router)
app.include_router(patient_router)
app.include_router(organization_router)
app.include_router(practitioner_router)
app.include_router(practitioner_role_router)
app.include_router(goal_router)
app.include_router(condition_router)
app.include_router(service_request_router)
app.include_router(observation_router)
app.include_router(encounter_router)
app.include_router(diagnostic_report_router)
