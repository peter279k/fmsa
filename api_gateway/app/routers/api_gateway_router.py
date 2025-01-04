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


api_gateway_router = APIRouter(prefix='/api/v1')
