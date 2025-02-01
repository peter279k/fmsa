from app.routers import *

from fastapi import FastAPI


description = '''
FHIR IG Manager is used to manage FHIR implementation guide
'''
app = FastAPI(
    title='FHIR IG Manager',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    }
)

app.include_router(manager_router)
