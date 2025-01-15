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

app.include_router(care_plan_router)
app.include_router(patient_router)
app.include_router(practitioner_router)
app.include_router(goal_router)
app.include_router(condition_router)
