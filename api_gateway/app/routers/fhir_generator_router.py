import json
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import File
from fastapi import Form
from fastapi import UploadFile
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from fastapi_gateway import route

from app.depends import check_api_key


fhir_generator_router = APIRouter(prefix='/api/v1/fhir_generator')

@route(
    request_method=fhir_generator_router.get,
    service_url=SERVICE_URLS[3],
    gateway_path='/check_required_header',
    service_path='/generate_care_plan',
    status_code=status.HTTP_200_OK,
    tags=['Check_api_key dependency for fhir_generator'],
)
async def check_required_header(request: Request):
    check_api_key(request)
    pass

