from app.item_models.track8_2024 import *
from app.item_models.track13_2024 import *
from app.modules import Track8ForObservation
from app.modules import Track13ForObservation

from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def generate_track13_2024_for_observation(item: Track13ForObservationModel):
    status_code = 200
    resource_name = 'Observation'
    item_dict = item.model_dump()
    observation_resource = {}

    try:
        track13_for_observation = Track13ForObservation.Track13ForObservation(resource_name, item_dict)
        observation_resource = track13_for_observation.generate_observation_resource()
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
            'message': 'Creating Observation resource for Track 13 is successful.',
            'data': [observation_resource],
        },
        status_code=status_code
    )

async def generate_track8_2024_for_observation(request: Request, item: Track8ForResource):
    status_code = 200
    resource_name = 'Observation'
    item_dict = item.model_dump()
    observation_resource = {}
    observation_type = request.query_params.get('type', '')

    try:
        track8_for_observation = Track8ForObservation.Track8ForObservation(resource_name, item_dict)
        if observation_type == 'imri-cancer-staging':
            observation_resource = track8_for_observation.generate_observation_cancer_staging_resource()
        else:
            observation_resource = track8_for_observation.generate_observation_resource()
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
            'message': 'Creating Observation resource for Track 8 is successful.',
            'data': [observation_resource],
        },
        status_code=status_code
    )
