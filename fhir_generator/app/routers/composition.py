from app.item_models.track8_2024 import *
from app.modules import Track8ForComposition

from fastapi.responses import JSONResponse


async def generate_track8_2024_for_composition(item: Track8ForResource):
    status_code = 200
    resource_name = 'Composition'
    item_dict = item.model_dump()
    composition_resource = {}

    try:
        track8_for_composition = Track8ForComposition.Track8ForComposition(resource_name, item_dict)
        composition_resource = track8_for_composition.generate_composition_resource()
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
            'message': 'Creating Composition resource for Track 8 is successful.',
            'data': [composition_resource],
        },
        status_code=status_code
    )
