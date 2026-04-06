from app.routers import *

from fastapi import FastAPI
from circuit_breaker import CircuitBreakerMiddleware, CircuitBreakerInputDto


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

app.add_middleware(
    CircuitBreakerMiddleware,
    circuit_breaker_input=CircuitBreakerInputDto(
        exception_list=(Exception,),
        half_open_retry_count=5,
        half_open_retry_timeout_seconds=60,
    ),
)

app.include_router(converter_router)
