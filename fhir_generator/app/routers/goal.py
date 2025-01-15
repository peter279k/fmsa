from app.item_models.track13_2024 import *
from app.modules import Track13ForServiceRequest

from fastapi.responses import JSONResponse


async def generate_track13_2024_for_service_request(item: Track13ForServiceRequestModel):
    status_code = 200
    resource_name = 'ServiceRequest'
    item_dict = item.model_dump()
    service_request_resource = {}

    try:
        track13_for_service_request = Track13ForServiceRequest.Track13ForServiceRequest(resource_name, item_dict)
        service_request_resource = track13_for_service_request.generate_service_request_resource()
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
            'message': 'Creating ServiceRequest resource for Track 13 is successful.',
            'data': [service_request_resource],
        },
        status_code=status_code
    )
