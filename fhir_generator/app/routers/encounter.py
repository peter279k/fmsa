from app.item_models.track8_2024 import *
from app.modules import Track8ForEncounter

from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def generate_track8_2024_for_encounter(request: Request, item: Track8ForResource):
    status_code = 200
    resource_name = 'Encounter'
    item_dict = item.model_dump()
    encounter_resource = {}
    encounter_type = request.query_params.get('type', '')

    try:
        track8_for_encounter = Track8ForEncounter.Track8ForEncounter(resource_name, item_dict)
        if encounter_type == 'imri-min':
            encounter_resource = track8_for_encounter.generate_encounter_min_resource()
        else:
            encounter_resource = track8_for_encounter.generate_encounter_resource()
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
            'message': 'Creating Encounter resource for Track 8 is successful.',
            'data': [encounter_resource],
        },
        status_code=status_code
    )
