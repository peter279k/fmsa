from app.routers import *

from fastapi import FastAPI


description = '''
FHIR Data Manager is used to create, read, update and delete these specific FHIR resources
'''
app = FastAPI(
    title='FHIR Data Manager',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    }
)

app.include_router(upload_resource_router)
app.include_router(retrieve_resource_router)
app.include_router(hapi_fhir_server_adapter_router)
