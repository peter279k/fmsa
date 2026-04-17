import os
import signal
import datetime
import clickhouse_connect

from app.routers import *

from fastapi import FastAPI
from contextlib import asynccontextmanager
from circuit_breaker import CircuitBreakerMiddleware, CircuitBreakerInputDto



description = '''
FHIR Generator is used to create the specific FHIR resources
'''


def custom_handler(signal_num):
    app.state.shutting_down = True
    print(f'FHIR Generator Received signal {signal_num}.')

signal.signal(signal.SIGTERM, custom_handler)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('FHIR Generator Application starting up...')

    yield

    print("FHIR Generator Application shutting down...")


app = FastAPI(
    title='FHIR Generator',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    },
    lifespan=lifespan
)

circuit_breaker_app = FastAPI(
    title='FHIR Circuit Breaker',
    description=description,
    version='1.0'
)

@circuit_breaker_app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    host = os.getenv('IP_ADDRESS', '172.17.0.1')
    client = clickhouse_connect.get_client(host=host, username='fmsa_exp', password='fmsa_exp')
    table_name = 'rq5_log_table_circuit'
    columns = ['timestamp', 'message_type', 'message', 'service_name', 'api_path']
    records = [
        [
            datetime.datetime.now(datetime.UTC), 'open/half-open state',
            f'503: {str(exc)}',
            'fhir_generator', 'ltc_tw_2025_location_circuit',
        ],
    ]
    client.insert(table_name, records, column_names=columns)
    client.close()

    return JSONResponse(
        status_code=503,
        content={'message': str(exc)},
    )

circuit_breaker_app.add_middleware(
    CircuitBreakerMiddleware,
    circuit_breaker_input=CircuitBreakerInputDto(
        exception_list=(Exception,),
        half_open_retry_count=5,
        half_open_retry_timeout_seconds=60,
    ),
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

circuit_breaker_app.include_router(location_router)
app.mount('/circuit', circuit_breaker_app)

app.include_router(claim_router)
app.include_router(location_router)
app.include_router(adverse_event_router)
app.include_router(document_reference_router)
app.include_router(imaging_study_router)
app.include_router(procedure_router)
app.include_router(medication_request_router)
app.include_router(medication_administration_router)
app.include_router(composition_router)
app.include_router(coverage_router)
app.include_router(care_plan_router)
app.include_router(patient_router)
app.include_router(organization_router)
app.include_router(practitioner_router)
app.include_router(practitioner_role_router)
app.include_router(questionnaire_response_router)
app.include_router(goal_router)
app.include_router(condition_router)
app.include_router(service_request_router)
app.include_router(observation_router)
app.include_router(encounter_router)
app.include_router(diagnostic_report_router)
app.include_router(directed_upload_router)
