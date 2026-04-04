from app.modules import HttpUploader
from app.item_models.data_payload import *

from fastapi.responses import JSONResponse


async def upload_observation_resource_data(item: DataPayload):
    status_code = 200
    resource_name = 'Observation'
    item_dict = item.model_dump()

    try:
        info = {
            'url': f'http://fhir_generator:8000/api/v1/directed_upload/{resource_name}',
            'body': item_dict['payload'],
            'header': {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
        }
        uploader = HttpUploader.HttpUploader()
        response = uploader.connect(info)
        processed_response = uploader.process(response)
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
        processed_response,
        status_code=processed_response['status']
    )
