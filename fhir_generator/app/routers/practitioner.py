from app.item_models.track8_2024 import *
from app.item_models.track13_2024 import *
from app.modules import Track8ForPractitioner
from app.modules import Track13ForPractitioner

from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def generate_track13_2024_for_practitioner(item: Track13ForPractitionerModel):
    status_code = 200
    resource_name = 'Practitioner'
    item_dict = item.model_dump()
    practitioner_resource = {}

    try:
        track13_for_practitioner = Track13ForPractitioner.Track13ForPractitioner(resource_name, item_dict)
        practitioner_resource = track13_for_practitioner.generate_practitioner_resource()
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
            'message': 'Creating Practitioner resource for Track 13 is successful.',
            'data': [practitioner_resource],
        },
        status_code=status_code
    )

async def generate_track8_2024_for_practitioner(request: Request, item: Track8ForResource):
    status_code = 200
    resource_name = 'Practitioner'
    item_dict = item.model_dump()
    practitioner_resource = {}

    practitioner_type = request.query_params.get('type', '')

    try:
        track8_for_practitioner = Track8ForPractitioner.Track8ForPractitioner(resource_name, item_dict)
        if practitioner_type == 'imri-min':
            practitioner_resource = track8_for_practitioner.generate_practitioner_name_resource()
        else:
            practitioner_resource = track8_for_practitioner.generate_practitioner_resource()
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
            'message': 'Creating Practitioner resource for Track 8 is successful.',
            'data': [practitioner_resource],
        },
        status_code=status_code
    )
