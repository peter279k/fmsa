from app.routers import *

from fastapi import FastAPI


description = '''
FHIR Profile Manager is used to manage FHIR profile and StructureDefinition
'''
app = FastAPI(
    title='FHIR Profile Manager',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    }
)

app.include_router(manager_router)
