from app.item_models.track8_2024 import *
from app.item_models.track13_2024 import *
from app.modules import Track8ForPatient
from app.modules import Track13ForPatient

from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def generate_track13_2024_for_patient(item: Track13ForPatientModel):
    status_code = 200
    resource_name = 'Patient'
    item_dict = item.model_dump()
    patient_resource = {}

    try:
        track13_for_patient = Track13ForPatient.Track13ForPatient(resource_name, item_dict)
        patient_resource = track13_for_patient.generate_patient_resource()
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [item_dict],
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': status_code,
            'message': 'Creating Patient resource for Track 13 is successful.',
            'data': [patient_resource],
        },
        status_code=status_code
    )

async def generate_track8_2024_for_patient(request: Request, item: Track8ForResource):
    status_code = 200
    resource_name = 'Patient'
    item_dict = item.model_dump()
    patient_resource = {}
    patient_type = request.query_params.get('type', '')

    try:
        track8_for_patient = Track8ForPatient.Track8ForPatient(resource_name, item_dict)
        if patient_type == 'imri-min':
            patient_resource = track8_for_patient.generate_patient_imri_min_resource()
        else:
            patient_resource = track8_for_patient.generate_patient_resource()
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [item_dict],
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': status_code,
            'message': 'Creating Patient resource for Track 8 is successful.',
            'data': [patient_resource],
        },
        status_code=status_code
    )
