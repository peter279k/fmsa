from fastapi import FastAPI
from starlette.requests import Request


app = FastAPI(title='FHIR Generator')


@app.get(
    path='/api/v1/generate_care_plan',
    tags=['Path'],
)
async def generate_care_plan(request: Request):
    return {}
