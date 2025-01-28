from app.item_models.track8_2024 import *
from app.modules import Track8ForLocation

from fastapi.responses import JSONResponse


async def generate_track8_2024_for_location(item: Track8ForResource):
    status_code = 200
    resource_name = 'Location'
    item_dict = item.model_dump()
    location_resource = {}

    try:
        track8_for_location = Track8ForLocation.Track8ForLocation(resource_name, item_dict)
        location_resource = track8_for_location.generate_location_resource()
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
            'message': 'Creating Location resource for Track 8 is successful.',
            'data': [location_resource],
        },
        status_code=status_code
    )
