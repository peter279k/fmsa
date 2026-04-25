from app.routers import *

from fastapi import FastAPI
from circuit_breaker import CircuitBreakerMiddleware, CircuitBreakerInputDto


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

'''
app.add_middleware(
    CircuitBreakerMiddleware,
    circuit_breaker_input=CircuitBreakerInputDto(
        exception_list=(Exception,),
        half_open_retry_count=5,
        half_open_retry_timeout_seconds=60,
    ),
)
'''

app.include_router(upload_resource_router)
app.include_router(delete_resource_router)
app.include_router(retrieve_resource_router)
app.include_router(hapi_fhir_server_adapter_router)
