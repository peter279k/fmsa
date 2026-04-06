from app.routers import *

from fastapi import FastAPI
from circuit_breaker import CircuitBreakerMiddleware, CircuitBreakerInputDto


description = '''
Data Analysis Service is used to calculate statistics value
'''
app = FastAPI(
    title='Data Analysis Service',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    }
)

# app.add_middleware(
#     CircuitBreakerMiddleware,
#     circuit_breaker_input=CircuitBreakerInputDto(
#         exception_list=(Exception,),
#         half_open_retry_count=5,
#         half_open_retry_timeout_seconds=60,
#     ),
# )

app.include_router(analysis_router)
