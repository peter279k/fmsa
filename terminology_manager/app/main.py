from app.routers import *

from fastapi import FastAPI


description = '''
FHIR Terminology Manager is used to manage FHIR terminology services
'''
app = FastAPI(
    title='FHIR Terminology manager',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    }
)

app.include_router(manager_router)
