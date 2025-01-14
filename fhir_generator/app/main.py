from app.routers import *

from fastapi import FastAPI
from starlette.requests import Request


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
