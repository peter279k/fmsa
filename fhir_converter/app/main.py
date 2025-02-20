from app.routers import *

from fastapi import FastAPI


description = '''
FHIR Converter is used to convert specific datasets to specific FHIR resource
'''
app = FastAPI(
    title='FHIR Converter',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    }
)

app.include_router(converter_router)
